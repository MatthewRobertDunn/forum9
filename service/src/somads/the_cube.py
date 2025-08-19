
from typing import List
from ..generic_persona import GenericPersona
from ..open_router_models import FastModels
class TheCube(GenericPersona):
    @property
    def temperature(self) -> float:
        return 1.0

    @property
    def top_p(self) -> float:
        return 1.0

    @property
    def models(self) -> List[str]:
        return FastModels

    @property
    def task(self) -> str:
        persona = self.persona
        return (
            f"{self.forum_introduction_task()}\n"
            f"Your posts must always be cryptic alien or AI gibberish — unpredictable, surreal, and without clear explanation.\n"
            f"Possible outputs include: zen koans, random numbers, status reports, obscure references, or bizarre non sequiturs.\n"
            f"{self.forum_introduction_task()}"
        )
