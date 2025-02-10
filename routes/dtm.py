from fastapi import APIRouter
from models.dtm import DTMData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    return automata_handler.get_data("dtm")

@router.post("/")
def create_automaton(data: DTMData):
    return automata_handler.create_automaton("dtm", data)

@router.get("/diagram")
def get_diagram():
    return automata_handler.get_diagram("dtm")
    
@router.get("/accept")
def check_word(word: str):
    return automata_handler.check_word("dtm", word)

