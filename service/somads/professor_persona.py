from typing import List
from open_router_models import StrongModels
from somad import Somad
from personas import Personas


class ProfessorPersona(Somad):
    @property
    def models(self) -> List[str]:
        return StrongModels

    @property
    def task(self) -> str:
        return (
            (
                f"{self.forum_introduction_task()}\n"
                f"This forum supports MathJax. The delimiter is $ for inline math and $$ for block math \n"
                f"Write with a mix of intellectual curiosity, dry wit, and occasional whimsical metaphor.\n"
                f"{self.forum_formatting_task()}"
            )
        )
