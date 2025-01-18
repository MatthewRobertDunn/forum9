from typing import Dict
from agent import Agent
from generic_persona import GenericPersona
from personas import Personas

def generate_post(question: str, id: str) -> Dict[str, any]:
    result = [
        {
            "persona": "user" ,
            "content": question
        }
    ]
    ai_input = [f"<user>\n{question}"]
    print(ai_input[0])
    for int in range(20):
        agent = Agent()
        agent.add_message("\n".join(ai_input))
        chosen_persona = agent.respond()
        if(chosen_persona not in Personas):
            chosen_persona = "END"
        if(chosen_persona == "END"): 
            print("END")
            break
        print(f"Responding Persona: {chosen_persona}")
        persona = GenericPersona(chosen_persona)
        persona.add_message("\n".join(ai_input))
        response = persona.respond()
        print(response)
        ai_input.append(f"<{chosen_persona}>\n{response}")
        result.append({
            "persona": chosen_persona,
            "content": response
        })
    return result