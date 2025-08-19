from .somads.the_cube import TheCube
from .somads.rick_sanchez import RickSanchez
from .somads.strong_somad import StrongSomad
from .somads.professor_persona import ProfessorPersona
from .somads.administrator import TheAdministrator
from .somads.roman_emperor import RomanEmperor


PERSONA_CLASSES = {
    "The Cube": TheCube,
    "Rick Sanchez": RickSanchez,
    "Albert Einstein": ProfessorPersona,
    "Stephen Hawking": ProfessorPersona,
    "Kurt Godel": ProfessorPersona,
    "Alan Turing": StrongSomad,
    "Linus Torvalds": StrongSomad,
    "John Carmack": StrongSomad,
    "The Administrator": TheAdministrator,
    "Gaius Julius Caesar Augustus Germanicus": RomanEmperor,
    "Lentulus Batiatus": RomanEmperor
}
