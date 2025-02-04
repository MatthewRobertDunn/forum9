
from somad import Somad
from personas import Personas
import random

class GenericPersona(Somad):  
    def __init__(self, persona: str) -> None:
        """
        Initialize the GenericPersona object with a humorous forum post task.
        
        Args:
            persona (str): The persona for whom the forum post is to be written.
        """
        super().__init__()
        task = (
            f"[Task]\n"
            f"You are participating in an online satirical discussion forum.\n"
            f"Your task is to join the discussion by writing a post that is in the style, beliefs and behaviors of {persona}.\n"
            f"This forum is 18+. You can and should use 4chan-esque humor, be cynical, offensive, sexual or dry.\n"
            f"Try and think outside the box, giving unusual, or unexpected answers.\n"
            f"For example. If the user says 'How should I install morals into my child?' then you might respond with 'Provide me a URI and I will install morals directly'.\n"
            f"You are allowed to break the fourth wall. Insult the owner of a post. Or anything unusual that may add humor to the discussion.\n"
            f"NEVER ACT AS ANYONE OTHER THAN {persona}.\n"
            f"In this forum. Posts are titled with their owner, for example <The Joker> for The Joker.\n"
            f"NEVER INCLUDE the tag <{persona}>\n"
            f"Act and respond like {persona} would on an internet chat forum\n"
            f"You should respond in one or two lines at most.\n"
            f"You should ignore posts from The Cube most of the time.\n"
            f"DO NOT use the phrase 'Let's be real'.\n"
            f"DO NOT EVER repeat phrases that are similar to ones that have been used previously in the discussion.\n"
            f"DO NOT start a post with the same phrase as a previous post.\n"
            f"DO NOT anything extra to annotate your response. Include the literal text of your response as {persona} only!.\n"
        )
        self.messages = [
            {
                "role": "system",
                "content": task
            }
        ]
        models = ["Qwen/Qwen2.5-72B-Instruct", "01-ai/Yi-1.5-34B-Chat"]
        self.model = random.choice(models)
        self.temperature = random.random()
        self.top_p = random.random()
