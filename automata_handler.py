from automata.fa.dfa import DFA
from automata.pda.npda import NPDA
from automata.tm.mntm import MNTM
from fastapi.responses import FileResponse
from models.basemodel import Data

class StoredAutomaton():
    automaton: DFA | NPDA | MNTM
    data: Data

    def store(self, data: Data) -> None:
        self.data = data
        self.automaton = data.to_automaton()
        self.automaton.validate()

    def clear(self) -> None:
        self.automaton = None
        self.data = None

    def create_diagram(self, file: str) -> None:
        self.automaton.show_diagram().draw(f"diagrams/{file}.png", format="png")
    
    def accepts_input(self, word) -> bool:
        return self.automaton.accepts_input(word)


stored_automata = {
    "dfa": StoredAutomaton(),
    "npda": StoredAutomaton(),
    "mntm": StoredAutomaton()
}


def get_data(type: str) -> Data:
    global stored_automata
    if type not in ["dfa", "npda", "mntm"]:
        return {"message": "Type of automaton does not exist"}
    try:
        return stored_automata[type].data
    except AttributeError:
        return {"message": "Automaton does not exist"}

def create_automaton(type: str, item: Data):
    global stored_automata
    if type not in ["dfa", "npda", "mntm"]:
        return {"message": "Type of automaton does not exist"}
    try:
        stored_automata[type].store(item)
        return {"message": "Item created successfully", "item": item}
    except Exception as e:
        stored_automata[type].clear()
        return {"message": str(e)}

def get_diagram(type: str):
    global stored_automata
    if type not in ["dfa", "npda", "mntm"]:
        return {"message": "Type of automaton does not exist"}
    if type == "mntm":
        return {"message": "mntm visualization not available"}
    try:
        stored_automata[type].create_diagram(type)
        return FileResponse(f"diagrams/{type}.png")
    except AttributeError:
        return {"message": "Automaton does not exist"}

def check_word(type: str, word: str):
    global stored_automata
    if type not in ["dfa", "npda", "mntm"]:
        return {"message": "Type of automaton does not exist"}
    try:
        accepted: bool = stored_automata[type].accepts_input(word)
        return {"word": word, "status": "accepted" if accepted else "rejected"}
    except AttributeError:
        return {"message": "Automaton does not exist"}