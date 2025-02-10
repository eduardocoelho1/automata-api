from automata.pda.dpda import DPDA, DPDATransitionsT
from typing import Literal
from models.basemodel import Data

class DPDAData(Data):
    stack_symbols: set[str]
    transitions: DPDATransitionsT
    initial_stack_symbol: str
    acceptance_mode: Literal["final_state", "empty_stack", "both"] = "both"

    def to_automaton(self) -> DPDA:
        return DPDA(
            states=self.states,
            input_symbols=self.input_symbols,
            stack_symbols=self.stack_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            initial_stack_symbol=self.initial_stack_symbol,
            final_states=self.final_states,
            acceptance_mode=self.acceptance_mode
        )