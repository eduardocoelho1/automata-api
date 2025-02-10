from fastapi import APIRouter
from models.dfa import DFAData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    """
    Returns the automaton data as a JSON text
    """
    return automata_handler.get_data("dfa")

@router.post("/")
def create_automaton(data: DFAData):
    """
    Creates a DFA using the provided JSON data.
    - **states**: Set of states
    - **input_symbols**: Set of input symbols
    - **transitions**: Dict of transitions
    - **initial_state**: Initial state
    - **final_states**: Set of final states
    - **allow_partial**: Allows states to not need to have a transition to every input symbol (optional) (default=false)
    """
    return automata_handler.create_automaton("dfa", data)

@router.get("/diagram")
def get_diagram():
    """
    Generates a diagram of the automaton
    """
    return automata_handler.get_diagram("dfa")
    
@router.get("/accept")
def check_word(word: str):
    """
    Checks whether a word is accepted and returns 'accepted' or 'rejected'
    """
    return automata_handler.check_word("dfa", word)

