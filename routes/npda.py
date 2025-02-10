from fastapi import APIRouter
from models.npda import NPDAData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    return automata_handler.get_data("npda")

@router.post("/")
def create_automaton(data: NPDAData):
    return automata_handler.create_automaton("npda", data)

@router.get("/diagram")
def get_diagram():
    return automata_handler.get_diagram("npda")
    
@router.get("/accept/{word}")
def check_word(word: str):
    return automata_handler.check_word("npda", word)