from pydantic import BaseModel
from abc import abstractmethod

class Data(BaseModel):
    states: set[str]
    input_symbols: set[str]
    initial_state: str
    final_states: set[str]

    @abstractmethod
    def to_automaton():
        pass
