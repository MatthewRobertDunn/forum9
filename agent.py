
from somad import Somad
from personas import Personas

task = f"""[Task]
I'm going to give you a conversation. And your job is to respond only with which persona would be best to respond to this conversation.
Respond by returning one of the personals from [The Personas] list and nothing else.
[The Personas]
{'\n'.join(Personas)}
"""
class Agent(Somad):  
    def __init__(self) -> None:
        super().__init__()
        self.messages = [
        {
                "role": "system",
                "content": task
        }]