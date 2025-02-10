from fastapi import APIRouter
from models.dpda import DPDAData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    return automata_handler.get_data("dpda")

@router.post("/")
def create_automaton(data: DPDAData):
    return automata_handler.create_automaton("dpda", data)

@router.get("/diagram")
def get_diagram():
    return automata_handler.get_diagram("dpda")
    
@router.get("/accept")
def check_word(word: str):
    return automata_handler.check_word("dpda", word)