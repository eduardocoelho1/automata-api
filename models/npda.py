from automata.pda.npda import NPDA, NPDATransitionsT
from typing import Literal
from models.basemodel import Data

class NPDAData(Data):
    stack_symbols: set[str]
    transitions: NPDATransitionsT
    initial_stack_symbol: str
    acceptance_mode: Literal["final_state", "empty_stack", "both"] = "both"

    def to_automaton(self) -> NPDA:
        return NPDA(
            states=self.states,
            input_symbols=self.input_symbols,
            stack_symbols=self.stack_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            final_states=self.final_states,
            acceptance_mode=self.acceptance_mode
        )