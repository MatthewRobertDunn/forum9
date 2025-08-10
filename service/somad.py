import random
import re
from typing import List, Optional, Tuple
from openai import OpenAI
from config import HUGGING_API_KEY
from model_pool import ModelPool
from model import Model
from retry_decorator import retry
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
        return [
            "meta-llama/llama-3.3-70b-instruct:free",
            "google/gemma-3-27b-it:free",
            "openai/gpt-oss-20b:free",
            "qwen/qwen3-235b-a22b:free",
            "qwen/qwen-2.5-72b-instruct:free",
            "deepseek/deepseek-r1-0528:free",
            "meta-llama/llama-3.1-405b-instruct:free",
            "deepseek/deepseek-chat-v3-0324:free",
            "qwen/qwen3-coder:free",
            "tngtech/deepseek-r1t2-chimera:free",
            "deepseek/deepseek-r1-distill-llama-70b:free",
            "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
        ]

    def __init__(self) -> None:
        self.allowed_models = [
            self.model_pool.get_model(name) for name in self.models]
        self.temperature = 0.5
        self.max_tokens = 4096
        self.top_p = 0.7
        self.messages = [
            {
                "role": "system",
                "content": """Intentionally empty, inherit from Somad to implement a presonality."""
            },
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
        exponent = 2  # tweak this to adjust bias strength
        r = random.random() ** exponent
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
            f"Selected model: {model.name} score {model.score} temperature: {self.temperature} top_p: {self.top_p} max_tokens: {self.max_tokens}")

        response_message = None
        try:
            response = client.chat.completions.create(
                model=model.name,
                messages=self.messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                timeout=120
            )
            response_message = response.choices[0].message
        except Exception as e:
            model.add_score(-1)
            raise
        text = response_message.content
        print("----raw response----")
        print(text)
        print("----raw response end----")
        text = re.sub(r"<think>.*?</think>", "", text,
                      flags=re.DOTALL | re.IGNORECASE)
        
        text = text.strip()
        # Score the response, penalize empty response
        if (len(text) > 0):
            model.add_score(1)
        else:
            model.add_score(-1)
        return text, model
