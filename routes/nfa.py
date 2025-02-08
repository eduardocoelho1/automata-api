from fastapi import APIRouter
from fastapi.responses import FileResponse
from automata.fa.nfa import NFA
from models.nfa import NFAData

stored_item: NFA = None

router = APIRouter()

@router.post("/")
def create_item(item: NFAData):
    global stored_item
    try:
        stored_item = item.to_nfa()
        stored_item.validate()
        return {"message": "Item created successfully", "item": item}
    except Exception as e:
        stored_item = None
        return {"message": str(e)}

@router.get("/diagram")
def read_item():
    try:
        stored_item.show_diagram().draw("diagrams/nfa.png", format="png")
        return FileResponse("diagrams/nfa.png")
    except AttributeError:
        return {"message": "Automaton does not exist"}
    
@router.get("/accept/{word}")
def read_item(word: str):
    try:
        accepted: bool = stored_item.accepts_input(word)
        return {"word": word, "status": "accepted" if accepted else "rejected"}
    except AttributeError:
        return {"message": "Automaton does not exist"}

