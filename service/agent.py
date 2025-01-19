
from somad import Somad
from personas import Personas

task = f"""[Task]
I'm going to give you a discussion forum. And your job is to respond only with the persona that would be best to respond to the last post
Respond by returning one of the personals from [The Personas] list and **NOTHING ELSE**
You should also select the persona that would be the most comedic to post next.
The ownder of a post will be indicated by a tag of the form <PERSONA>
Avoid selecting a persona to respond to their own post
Do not use any tags in your response such as the <PERSONA> tag
If the discussion is long enough and has come to a natural stopping point, respond with END
The discussion forum is 18+ and satirical. Don't worry about being offensive.
Never respond with END until there is at least one <PERSONA> tag in the dicussion.
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