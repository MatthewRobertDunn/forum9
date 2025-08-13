from typing import Dict, List
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

persona_classes = {
    "The Cube": TheCube.TheCube,
    "Rick Sanchez": RickSanchez.RickSanchez,
    "Albert Einstein": StrongSomad.StrongSomad,
    "Stephen Hawking": StrongSomad.StrongSomad,
    "Kurt Godel": StrongSomad.StrongSomad,
    "Alan Turing": StrongSomad.StrongSomad,
    "Linus Torvalds": StrongSomad.StrongSomad,
    "John Carmack": StrongSomad.StrongSomad
}


class ParseResponseResult:
    def __init__(self, content: str, ai_clean: bool):
        self.content = content
        self.ai_clean = ai_clean

def choose_persona(choice: str, personas: List[str]) -> str:
    for persona in random.sample(personas, len(personas)):
        if persona in choice:
            return persona
    return None

def generate_post(question: str, id: str) -> Dict[str, any]:
    personas_and_end = Personas + ["END"]
    result = []
    ai_input = [f"<user>\n{question}"]
    print(ai_input[0])
    respond_with(result, ai_input, "The Cube")
    max_posts = random.randint(1, 20) + 2
    print(f"Max posts: {max_posts}")
    while len(result) < max_posts:
        agent = Agent()
        agent.add_message("\n".join(ai_input))
        agent_response, agent_model = agent.respond_with_model()
        chosen_persona = choose_persona(agent_response, personas_and_end)
        if (chosen_persona):
            print("Chosen persona is valid")
        else:
            print("Invalid Persona. Selecting at random")
            agent_model.add_score(-2)
            chosen_persona = random.choice(Personas)

        if (chosen_persona == "END"):
            print("END")
            if(len(result) > 2):
                break
            break

        respond_with(result, ai_input, chosen_persona)
    return result


def respond_with(result: list, ai_input: list, chosen_persona: str):
    persona = get_persona(chosen_persona)
    print(f"Responding Persona: {chosen_persona}")
    persona.add_message("\n".join(ai_input + [f"<{chosen_persona}>\n"]))
    response = parse_response(persona.respond())
    ai_input.append(f"<{chosen_persona}>\n{response.content}")
    cleaned_response = None
    if response.ai_clean:
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
    result.append({
        "persona": chosen_persona,
        "content": cleaned_response
    })


def get_persona(persona: str) -> Somad:
    if persona in persona_classes:
        return persona_classes[persona](persona)
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
    use_ai = True
    for line in headerless_response.split("\n"):
        stripped_line = line.strip()
        if stripped_line.startswith("<") and line.endswith(">"):
            persona = stripped_line[1:-1]
            if persona in personas_and_user:
                print("AI returned more than one response, skipping rest of response")
                break

        if (line.endswith("  ")):
            use_ai = False

        if (line.startswith("#")):
            use_ai = False

        if (line.startswith("```")):
            use_ai = False

        if (line.startswith("```")):
            use_ai = False

        result.append(line)

    if (len(result) <= 1):
        use_ai = False

    return ParseResponseResult("\n".join(result), use_ai)
