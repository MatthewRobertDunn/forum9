
from somad import Somad
from personas import Personas
import random


class GenericPersona(Somad):
    @property
    def task(self) -> str:
        persona = self.persona
        return (
            f"{self.forum_introduction_task(persona)}\n"
            f"Requirements:\n"
            f"- Posts here are tagged with their author's name, except yours: never include the tag <{persona}> in your responses.\n"
            f"- Always respond exactly as {persona}, never as anyone else.\n"
            f"- Avoid acknowledging or responding to posts by “The Cube” unless explicitly relevant.\n"
            f"- Do not add any annotations, explanations, or formatting—only the literal post text as {persona}.\n"
        )
    
    @property
    def temperature(self) -> float:
        return random.random()

    @property
    def top_p(self) -> float:
        return random.random()
    
    def forum_introduction_task(self, persona: str) -> str:
        return (f"[Task]\n"
                f"You are participating in an 18+ online casual discussion forum. Your role is to post as {persona}, fully embodying their style, beliefs, and behaviors.\n"
                f"This forum supports CommonMark Markdown and MathJax syntax. MathJax is delimited by $$ for blocks and $ for inlines. \n"
                f"\n")
