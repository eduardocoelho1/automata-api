from fastapi import APIRouter
from models.dpda import DPDAData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    """
    Returns the automaton data as a JSON text
    """
    return automata_handler.get_data("dpda")

@router.post("/")
def create_automaton(data: DPDAData):
    """
    Creates a DPDA using the provided JSON data.
    - **states**: Set of states
    - **input_symbols**: Set of input symbols
    - **stack_symbols**: Set of stack symbols
    - **transitions**: Dict of transitions
    - **initial_state**: Initial state
    - **initial_stack_symbol**: Initial symbol on the stack
    - **final_states**: Set of final states
    - **acceptance_mode**: Acceptance mode: 'final_state', 'empty_stack', or 'both' (optional) (default='both')
    """
    return automata_handler.create_automaton("dpda", data)

@router.get("/diagram")
def get_diagram():
    """
    Generates a diagram of the automaton
    """
    return automata_handler.get_diagram("dpda")
    
@router.get("/accept")
def check_word(word: str):
    """
    Checks whether a word is accepted and returns 'accepted' or 'rejected'
    """
    return automata_handler.check_word("dpda", word)