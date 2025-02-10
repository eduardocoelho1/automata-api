from automata.tm.dtm import DTM, DTMTransitionsT
from models.basemodel import Data

class DTMData(Data):
    tape_symbols: set[str]
    transitions: DTMTransitionsT
    blank_symbol: str
    
    def to_automaton(self) -> DTM:
        return DTM(
            states=self.states,
            input_symbols=self.input_symbols,
            tape_symbols=self.tape_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            blank_symbol=self.blank_symbol,
            final_states=self.final_states
        )
