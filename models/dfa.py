from automata.fa.dfa import DFA, DFATransitionsT
from models.basemodel import Data

class DFAData(Data):
    transitions: DFATransitionsT
    allow_partial: bool = False
    
    def to_automaton(self) -> DFA:
        return DFA(
            states=self.states,
            input_symbols=self.input_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            final_states=self.final_states,
            allow_partial=self.allow_partial
        )
