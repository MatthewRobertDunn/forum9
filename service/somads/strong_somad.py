import random
from personas import Personas
from somad import Somad
from open_router_models import StrongModels
import os
import sys
from typing import List
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class StrongSomad(Somad):
    @property
    def models(self) -> List[str]:
        return StrongModels
