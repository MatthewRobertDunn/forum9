
from somad import Somad
from personas import Personas
import random

class MarkdownPersona(Somad):  
    def __init__(self) -> None:
        super().__init__()
        task ="""Your task is to clean up the formatting of a forum post.
DO NOT REMOVE ANYTHING. INCLUDE EVERYTHING IN THE REQUEST LITERALLY
DO NOT ADD COMMENTARY OR EXPLAIN WHAT YOU ARE DOING.
EVERYTHING IN THE INPUT NEEDS TO BE INCLUDED IN THE OUTPUT
RESPOND ONLY WITH THE FULL CONTENT FROM THE PROVIDED POST. 
You should:
*Reformat the post using Markdown
*Only return the first response given by a persona in the post
*Remember Markdown linebreaks are indicated by a \
*Reformat EVERYTHING provided literally. Not just content in the ``` blocks
For example, if a post looks like the following:
  This is a post by The Joker.
  <Einstein>
  E=mc^2 is my most famous equation"""
        self.messages = [
            {
                "role": "system",
                "content": task
            }
        ]
        self.model = "Qwen/Qwen2.5-72B-Instruct"