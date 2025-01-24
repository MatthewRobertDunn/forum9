from typing import Dict
from agent import Agent
from generic_persona import GenericPersona
from markdown_persona import MarkdownPersona
from personas import Personas
import random
import re

def generate_post(question: str, id: str) -> Dict[str, any]:
    personas_and_end = Personas + ["END"]
    result = []
    ai_input = [f"<user>\n{question}"]
    print(ai_input[0])
    max_posts = random.randint(1, 20)
    for i in range(max_posts):
        agent = Agent()
        print(f"Agent model is {agent.model}")
        agent.add_message("\n".join(ai_input))
        chosen_persona = agent.respond().strip()
        chosen_persona = chosen_persona.replace('<', '').replace('>', '')
        if(chosen_persona not in personas_and_end):
            print("Invalid Persona. Selecting at random")
            chosen_persona = random.choice(Personas)
        else:
            print("Chosen persona is valid")
        if(chosen_persona == "END"): 
            print("END")
            break
        persona = GenericPersona(chosen_persona)
        print(f"Responding Persona: {chosen_persona} with model {persona.model} top_p {persona.top_p} temperature {persona.temperature}")
        persona.add_message("\n".join(ai_input + [f"<{chosen_persona}>\n"]))
        response = parse_response(persona.respond())
        print(response)
        ai_input.append(f"<{chosen_persona}>\n{response}")
        result.append({
            "persona": chosen_persona,
            "content": response
        })
    return result



def parse_response(response: str) -> str:
    """
    Parse the response from a persona by extracting only the first valid response.
    Ignores additional persona responses beyond the first one.

    :param response: The response from a persona
    :return: The cleaned and parsed response
    """
    personas_and_user = Personas + ["user"]
    result = []
    headerless_response = re.sub(r'^<[^>]+>', '', response, count=1).strip()
    for line in headerless_response.split("\n"):
        stripped_line = line.strip()
        if stripped_line.startswith("<") and line.endswith(">"):
            persona = stripped_line[1:-1]
            if persona in personas_and_user:
                print("AI returned more than one response, skipping rest of response")
                break
        result.append(line)
    return "\\\n".join(result).strip()