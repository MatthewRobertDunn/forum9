import random
import re
from typing import List, Optional, Tuple
from openai import OpenAI
from config import HUGGING_API_KEY
from model_pool import ModelPool
from model import Model
from retry_decorator import retry
from open_router_models import GeneralModels, StrongModels
client = OpenAI(api_key=HUGGING_API_KEY,
                base_url="https://openrouter.ai/api/v1")


class Somad:
    _model_pools = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._model_pools[cls] = ModelPool()
        print(f"Created ModelPool for subclass {cls.__name__}")

    @property
    def model_pool(self):
        # Return the pool specific to this instance’s class
        return self._model_pools[self.__class__]

    @property
    def models(self) -> List[str]:
        # Base list of models — subclasses can override this
        return GeneralModels

    @property
    def temperature(self) -> float:
        return 0.5

    @property
    def top_p(self) -> float:
        return 0.7

    @property
    def task(self) -> str:
        return ""

    @property
    def model_bias_exponent(self) -> float:
        return 2.0

    def __init__(self, persona: str = None) -> None:
        self.allowed_models = [
            self.model_pool.get_model(name) for name in self.models]

        for model in self.allowed_models:
            if (model.name in StrongModels):
                model.max_tokens = 32768

        self.persona = persona

        self.messages = [
            {
                "role": "system",
                "content": self.task
            }
        ]

    def add_message(self, content: str):
        new_message = {
            "role": "user",
            "content": content
        }

        self.messages.append(new_message)

    def select_model(self) -> Optional[Model]:
        models = sorted(self.allowed_models,
                        key=lambda m: m.score, reverse=True)
        if not models:
            return None
        r = random.random() ** self.model_bias_exponent
        index = int(r * len(models))
        return models[index]

    def respond(self) -> Optional[str]:
        text, _ = self.respond_with_model()
        return text

    @retry(times=3, exceptions=(Exception,))
    def respond_with_model(self) -> Tuple[Optional[str], Optional[Model]]:
        model = self.select_model()
        if not model:
            print("No allowed models available")
            return None, None
        print(
            f"Selected model: {model.name} score {model.score} temperature: {self.temperature} top_p: {self.top_p} max_tokens: {model.max_tokens}")

        text = ""
        try:
            response = client.chat.completions.create(
                model=model.name,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=model.max_tokens,
                top_p=self.top_p,
                timeout=10,
                stream=True
            )
            for chunk in response:
                # The event can have 'choices' with 'delta' objects
                for choice in chunk.choices:
                    delta = choice.delta.content
                    if delta:
                        print(".", end="", flush=True)
                        text += delta
            print()
        except Exception as e:
            #penalize the model on any failures so a new model is selected next time
            model.add_score(-1)
            raise
        print("----raw response----")
        print(text)
        print("----raw response end----")

        #Remove unnecessary reasoning from the response
        text = re.sub(r"<think>.*?</think>", "", text,
                      flags=re.DOTALL | re.IGNORECASE)

        text = text.strip()
        # Score the response, penalize empty response
        if (len(text) > 0):
            model.add_score(1)
        else:
            model.add_score(-1)
        return text, model
