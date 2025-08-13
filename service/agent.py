
import random
from typing import List
from open_router_models import FastModels
from somad import Somad
from personas import Personas

task = f"""[Task]
You will be given an ongoing discussion from a forum. Your task is to select the single most appropriate persona to reply to the last post.
Follow these rules exactly:
* Choose only from the personas listed in [The Personas].
* Respond with **only** a single line containing either the chosen persona's name or END — no extra text, punctuation, or formatting.
* Posts identify their authors using tags in the form <PERSONA> at the start of a line.
* Do NOT choose the persona who authored the last post
* Do NOT include any tags such as <PERSONA> in your response.
* If the discussion contains at least two different personas and:
    - the last post contains no direct question, request, or disagreement,
    - and the tone suggests a natural conclusion to the discussion, output END instead.
[The Personas]
{chr(10).join(random.sample(Personas, len(Personas)))}
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
