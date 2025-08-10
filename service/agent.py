
from somad import Somad
from personas import Personas

task = f"""[Task]
You will be given an ongoing discussion forum. Your job is to respond **only** with the name of the persona best suited to reply to the last post.
- Choose from the personas listed under [The Personas].
- Respond with **only** the chosen persona’s name; do not add anything else.
- Select the persona that would provide the most comedic and engaging next post.
- Posts identify their owners with tags like <PERSONA>.
- Do **not** select the same persona who made the last post.
- Do **not** include any tags such as <PERSONA> in your response.
- The forum is 18+ and satirical; do not hesitate to be offensive if it fits.
- Respond with END only if the discussion has at least two different <PERSONA> tags and appears to have reached a natural conclusion.
[The Personas]
{chr(10).join(Personas)}
"""
class Agent(Somad):  
    def __init__(self) -> None:
        super().__init__()
        self.messages = [
        {
                "role": "system",
                "content": task
        }]