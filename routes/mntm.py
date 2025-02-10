from fastapi import APIRouter
from models.mntm import MNTMData
import automata_handler

router = APIRouter()

@router.get("/")
def get_data():
    return automata_handler.get_data("mntm")

@router.post("/")
def create_automaton(data: MNTMData):
    return automata_handler.create_automaton("mntm", data)

@router.get("/diagram")
def get_diagram():
    return automata_handler.get_diagram("mntm")
    
@router.get("/accept/{word}")
def check_word(word: str):
    return automata_handler.check_word("mntm", word)

