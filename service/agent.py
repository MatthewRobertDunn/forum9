
import random
from typing import List
from open_router_models import FastModels
from somad import Somad
from personas import Personas

task = f"""[Task]
You will be given an ongoing discussion forum. Your job is to respond **only** with the name of the persona best suited to reply to the last post.
- Choose from the personas listed under [The Personas].
- Respond with **only** a single line containing either the chosen persona’s name or 'END' do not add anything else.
- Posts identify their owners with tags like <PERSONA>.
- Do **not** select the same persona who made the last post.
- Do **not** include any tags such as <PERSONA> in your response.
- Respond with END if the discussion has at least two different <PERSONA> tags and appears to have reached a natural conclusion.
[The Personas]
{chr(10).join(Personas)}
"""


class Agent(Somad):
    @property
    def models(self) -> List[str]:
        return FastModels

    @property
    def model_bias_exponent(self) -> float:
        return 3.0

    def __init__(self) -> None:
        super().__init__()
        self.messages = [
            {
                "role": "system",
                "content": task
            }]
