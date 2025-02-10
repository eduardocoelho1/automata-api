from fastapi import APIRouter
from models.dtm import DTMData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    """
    Returns the automaton data as a JSON text
    """
    return automata_handler.get_data("dtm")

@router.post("/")
def create_automaton(data: DTMData):
    """
    Creates a DTM using the provided JSON data.
    - **states**: Set of states
    - **input_symbols**: Set of input symbols
    - **tape_symbols**: Set of tape symbols
    - **transitions**: Dict of transitions
    - **initial_state**: Initial state
    - **blank_symbol**: A symbol from 'tape_symbols' to be used as the blank symbol
    - **final_states**: Set of final states
    """
    return automata_handler.create_automaton("dtm", data)

@router.get("/accept")
def check_word(word: str):
    """
    Checks whether a word is accepted and returns 'accepted' or 'rejected'
    """
    return automata_handler.check_word("dtm", word)

