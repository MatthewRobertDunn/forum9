from agent import Agent
from generic_persona import GenericPersona
from personas import Personas

post = ["""<user>
What is Doctor Hannibal Lecter a doctor of, exactly?
"""]
print(post[0])
for int in range(20):
    agent = Agent()
    agent.add_message("\n".join(post))
    chosen_persona = agent.respond()
    if(chosen_persona not in Personas):
        chosen_persona = "END"
    if(chosen_persona == "END"): 
        print("END")
        break
    print(f"Responding Persona: {chosen_persona}")
    persona = GenericPersona(chosen_persona)
    persona.add_message("\n".join(post))
    response = persona.respond()
    print(response)
    post.append(f"<{chosen_persona}>\n{response}")