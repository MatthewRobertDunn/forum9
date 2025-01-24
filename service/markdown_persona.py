
from somad import Somad
from personas import Personas
import random

class MarkdownPersona(Somad):  
    def __init__(self) -> None:
        super().__init__()
        task = (
            f"[Task]\n"
            f"Your task is to clean up the formatting of a forum post.\n"
            f"DO NOT ALTER THE CONTENT OR ADD OR REMOVE ANYTHING OTHER THAN AS EXPLICITLY DESCRIBED HERE"
            f"RESPOND ONLY WITH CONTENT FROM THE PROVIDED POST. DO NOT ADD COMMENTARY OR EXPLAIN WHAT YOU ARE DOING.\n"
            f"You should:\n"
            f"*Reformat the post using Markdown\n"
            f"*Only return the first response given by a persona in the post\n"
            f"For example, if a post looks like the following:\n"
            f"  This is a post by The Joker.\n"
            f"  <Einstein>\n"
            f"  E=mc^2 is my most famous equation\n"
        )
        self.messages = [
            {
                "role": "system",
                "content": task
            }
        ]
        self.model = "01-ai/Yi-1.5-34B-Chat"