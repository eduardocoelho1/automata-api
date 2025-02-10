from fastapi import APIRouter
from fastapi.responses import FileResponse
from automata.pda.npda import NPDA
from models.npda import NPDAData

stored_item: NPDA = None
stored_item_data: NPDAData = None

router = APIRouter()

@router.post("/")
def create_item(item: NPDAData):
    global stored_item, stored_item_data
    try:
        stored_item_data
        stored_item = item.to_npda()
        stored_item.validate()
        return {"message": "Item created successfully", "item": item}
    except Exception as e:
        stored_item_data = None
        stored_item = None
        return {"message": str(e)}

@router.get("/diagram")
def read_item():
    try:
        stored_item.show_diagram().draw("diagrams/npda.png", format="png")
        return FileResponse("diagrams/npda.png")
    except AttributeError:
        return {"message": "Automaton does not exist"}
    
@router.get("/accept/{word}")
def read_item(word: str):
    try:
        accepted: bool = stored_item.accepts_input(word)
        return {"word": word, "status": "accepted" if accepted else "rejected"}
    except AttributeError:
        return {"message": "Automaton does not exist"}

