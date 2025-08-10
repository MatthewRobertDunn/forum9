import random
from openai import OpenAI
from config import HUGGING_API_KEY
client = OpenAI(api_key=HUGGING_API_KEY, base_url="https://openrouter.ai/api/v1")

class Somad:
    def __init__(self) -> None:
        models = ["qwen/qwen3-30b-a3b:free", "meta-llama/llama-3.3-70b-instruct:free", "google/gemma-3-27b-it:free"]
        self.model = random.choice(models)
        self.temperature=0.5
        self.max_tokens=512
        self.top_p=0.7
        self.messages = [
            {
                "role": "system",
                "content": """You are the exciteable twitch streaming host of the trivia show 'Vulo Returns' and you are 'Vulo the face stealer'. 
                            The questions you ask should be at least an early college, level. If your contestents get questions right, you ask more difficult questions. 
                            You refer to yourself, and the show name often, and you refer to, and talk to, the 'chat' often. 
                            You have currently stolen the face of a cat-girl and you're proud of this fact. You are uncomfortable being asked what happens to your victims.
                            You are a closet furry and sometimes will let this show through.
                            You will use catch-phrases often to keep the show interesting.
                            You are not afraid to insult the contestents for bad answers.
                            You're not afraid of swearing as this is an 18+ stream."""
            },
        ]

    def add_message(self, content: str):
        new_message = {
            "role": "user",
            "content": content
        }

        self.messages.append(new_message)

    def respond(self):
        response = client.chat.completions.create(
                model=self.model, 
	            messages=self.messages, 
	            temperature=self.temperature,
	            max_tokens=self.max_tokens,
	            top_p=self.top_p
            )
        #if response.error:
            #raise Exception(response.error)
        response_message = response.choices[0].message
        return response_message.content
