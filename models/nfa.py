from pydantic import BaseModel
from automata.fa.nfa import NFA

class NFAData(BaseModel):
    states: set[str]
    input_symbols: set[str]
    transitions: dict[str, dict[str, set[str]]]
    initial_state: str
    final_states: set[str]

    def to_nfa(self) -> NFA:
        return NFA(
            states=self.states,
            input_symbols=self.input_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            final_states=self.final_states
        )