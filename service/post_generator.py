from typing import Dict, List, Optional
from agent import Agent
from generic_persona import GenericPersona
from markdown_persona import MarkdownPersona
from personas import Personas
from somad import Somad
import somads.the_cube as TheCube
import somads.rick_sanchez as RickSanchez
import somads.strong_somad as StrongSomad
import random
import re

PERSONA_CLASSES = {
    "The Cube": TheCube.TheCube,
    "Rick Sanchez": RickSanchez.RickSanchez,
    "Albert Einstein": StrongSomad.StrongSomad,
    "Stephen Hawking": StrongSomad.StrongSomad,
    "Kurt Godel": StrongSomad.StrongSomad,
    "Alan Turing": StrongSomad.StrongSomad,
    "Linus Torvalds": StrongSomad.StrongSomad,
    "John Carmack": StrongSomad.StrongSomad
}

PERSONAS_AND_END = Personas + ["END"]


class ParseResponseResult:
    def __init__(self, content: str, ai_clean_post: bool):
        self.content = content
        self.ai_clean_post = ai_clean_post


def choose_persona(choice: str) -> Optional[str]:
    for persona in random.sample(PERSONAS_AND_END, len(PERSONAS_AND_END)):
        if persona in choice:
            return persona
    return None


def validate_persona_choice(chosen_persona: Optional[str], discussion: List[Dict[str, str]],) -> bool:
    if (not chosen_persona):
        print("No persona selected")
        return False

    if (chosen_persona and len(discussion) > 1 and chosen_persona == discussion[-1]["persona"]):
        print("Repeated persona")
        return False

    if (chosen_persona == "END" and len(discussion) <= 3):
        print("Too early to end")
        return False

    return True


def generate_discussion(question: str, id: str) -> List[Dict[str, str]]:
    discussion: List[Dict[str, str]] = []
    ai_input = [f"<user>\n{question}"]
    print(ai_input[0])
    append_persona_post(discussion, ai_input, "The Cube")
    max_posts = random.randint(1, 20) + 2
    print(f"Max posts: {max_posts}")
    while len(discussion) < max_posts:
        agent = Agent()
        agent.add_message("\n".join(ai_input))
        agent_response, agent_model = agent.respond_with_model()
        chosen_persona = choose_persona(agent_response)
        if (not validate_persona_choice(chosen_persona, discussion)):
            print("Persona choice is invalid -- selecting random persona")
            # Penalize the model for selecting poorly
            agent_model.add_score(-2)
            chosen_persona = random.choice(Personas)
        if (chosen_persona == "END"):
            print("AI chose to end discussion")
            break
        append_persona_post(discussion, ai_input, chosen_persona)
    
    print("Ending discussion")
    return discussion


def append_persona_post(discussion: List[Dict[str, str]], ai_input: List[str], chosen_persona: str):
    persona = get_persona(chosen_persona)
    print(f"Responding Persona: {chosen_persona}")
    persona.add_message("\n".join(ai_input + [f"<{chosen_persona}>\n"]))
    response = parse_response(persona.respond())
    ai_input.append(f"<{chosen_persona}>\n{response.content}")
    if response.ai_clean_post:
        print("Using markdown persona to clean response")
        markdown_persona = MarkdownPersona()
        markdown_persona.add_message(response.content)
        cleaned_response = markdown_persona.respond()
    else:
        cleaned_response = response.content

    print("----cleaned response----")
    print(cleaned_response)
    print("----cleaned response end----")

    if (not cleaned_response or len(cleaned_response.strip()) == 0):
        print("Skipping empty response")
        return
    discussion.append({
        "persona": chosen_persona,
        "content": cleaned_response
    })


def get_persona(persona: str) -> Somad:
    if persona in PERSONA_CLASSES:
        return PERSONA_CLASSES[persona](persona)
    else:
        return GenericPersona(persona)


def parse_response(response: str) -> ParseResponseResult:
    """
    Parse the response from a persona by extracting only the first valid response.
    Ignores additional persona responses beyond the first one.

    :param response: The response from a persona
    :return: The cleaned and parsed response
    """
    response = response.strip()
    personas_and_user = Personas + ["user"]
    result = []
    headerless_response = re.sub(r'^<[^>]+>', '', response, count=1).strip()
    ai_clean_post = True
    for line in headerless_response.split("\n"):
        stripped_line = line.strip()
        if stripped_line.startswith("<") and line.endswith(">"):
            persona = stripped_line[1:-1]
            if persona in personas_and_user:
                print("AI returned more than one response, skipping rest of response")
                break

        # detect if the post generation AI is already using markdown, in which case don't reformat it using ai
        if line.endswith("  ") or line.startswith(("#", "```")):
            ai_clean_post = False

        result.append(line)

    if (len(result) <= 1):
        ai_clean_post = False

    return ParseResponseResult("\n".join(result), ai_clean_post)
