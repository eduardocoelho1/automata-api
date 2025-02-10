from fastapi import APIRouter
from models.dfa import DFAData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    return automata_handler.get_data("dfa")

@router.post("/")
def create_automaton(data: DFAData):
    return automata_handler.create_automaton("dfa", data)

@router.get("/diagram")
def get_diagram():
    return automata_handler.get_diagram("dfa")
    
@router.get("/accept/{word}")
def check_word(word: str):
    return automata_handler.check_word("dfa", word)

