import random
from generic_persona import GenericPersona
from open_router_models import StrongModels
import os
import sys
from typing import List
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class StrongSomad(GenericPersona):
    @property
    def temperature(self) -> float:
        return 0.6

    @property
    def top_p(self) -> float:
        return 0.8

    @property
    def models(self) -> List[str]:
        return StrongModels
