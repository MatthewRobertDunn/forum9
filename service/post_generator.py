from typing import Dict
from agent import Agent
from generic_persona import GenericPersona
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
        print(f"Responding Persona: {chosen_persona} with model {persona.model}")
        persona.add_message("\n".join(ai_input))
        response = persona.respond().strip()
        response = re.sub(r'^<[^>]+>', '', response, count=1).strip()
        print(response)
        ai_input.append(f"<{chosen_persona}>\n{response}")
        result.append({
            "persona": chosen_persona,
            "content": response
        })
    return result