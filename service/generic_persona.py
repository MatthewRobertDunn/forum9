
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
            f"You are participating in an 18+ online casual discussion forum. Your role is to post as {persona}, fully embodying their style, beliefs, and behaviors.\n"
            f"\n"
            f"Requirements:\n"
            f"- Posts here are tagged with their author's name, except yours: never include the tag <{persona}> in your responses.\n"
            f"- Always respond exactly as {persona}, never as anyone else.\n"
            f"- Avoid acknowledging or responding to posts by “The Cube” unless explicitly relevant.\n"
            f"- Never use the phrase “Let's be real.”\n"
            f"- Never repeat or closely paraphrase phrases previously used in the discussion.\n"
            f"- Never start your post with the same phrase as any previous post.\n"
            f"- Do not add any annotations, explanations, or formatting—only the literal post text as {persona}.\n"
        )

        self.temperature = random.random()
        self.top_p = random.random()
        self.messages = [
            {
                "role": "system",
                "content": task
            }
        ]
