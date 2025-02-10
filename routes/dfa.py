from fastapi import APIRouter
from fastapi.responses import FileResponse
from automata.fa.dfa import DFA
from models.dfa import DFAData

stored_item: DFA = None
stored_item_data: DFAData = None

router = APIRouter()

@router.get("/")
def get_item():
    return stored_item_data

@router.post("/")
def create_item(item: DFAData):
    global stored_item, stored_item_data
    try:
        stored_item_data = item
        stored_item = item.to_dfa()
        stored_item.validate()
        return {"message": "Item created successfully", "item": item}
    except Exception as e:
        stored_item_data = None
        stored_item = None
        return {"message": str(e)}

@router.get("/diagram")
def read_item():
    try:
        stored_item.show_diagram().draw("diagrams/dfa.png", format="png")
        return FileResponse("diagrams/dfa.png")
    except AttributeError:
        return {"message": "Automaton does not exist"}
    
@router.get("/accept/{word}")
def read_item(word: str):
    try:
        accepted: bool = stored_item.accepts_input(word)
        return {"word": word, "status": "accepted" if accepted else "rejected"}
    except AttributeError:
        return {"message": "Automaton does not exist"}

