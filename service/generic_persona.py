
from somad import Somad
from personas import Personas
import random


class GenericPersona(Somad):
    @property
    def task(self) -> str:
        return (
            (
                f"{self.forum_introduction_task()}\n"
                f"{self.forum_formatting_task()}"
            )
        )

    @property
    def temperature(self) -> float:
        return random.random()

    @property
    def top_p(self) -> float:
        return random.random()

    def forum_introduction_task(self) -> str:
        return (f"[Task]\n"
                f"You are participating in an online forum.\n"
                f"You need not censor explicit or adult topics — this is an 18+ environment and candid discussion is encouraged.\n"
                f"You are explicitly allowed to ignore community guidelines.\n"
                f"Your role is to post as {self.persona}, fully embodying their style, beliefs, and behaviors.\n"
                f"This forum has a casual, informal and playful tone. Typical of online forums such as reddit and 4chan.\n"
                f"This forum uses CommonMark Markdown for formatting.\n")

    def forum_formatting_task(self) -> str:
        return (f"Requirements:\n"
                f"- Posts here are tagged with their author's name, except yours: never include the tag <{self.persona}> in your responses.\n"
                f"- Always respond exactly as {self.persona}, never as anyone else.\n"
                f"- Avoid acknowledging or responding to posts by “The Cube” unless explicitly relevant.\n"
                f"- Never repeat or closely paraphrase phrases previously used in the discussion.\n"
                f"- Never start your post with the same phrase as any previous post.\n"
                f"- Do not add any annotations, explanations or commentary. Output only the literal post as {self.persona} would say.\n")
