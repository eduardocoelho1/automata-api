from automata.tm.mntm import MNTM, MNTMTransitionsT
from models.basemodel import Data

class MNTMData(Data):
    tape_symbols: set[str]
    n_tapes: int
    transitions: MNTMTransitionsT
    blank_symbol: str
    
    def to_automaton(self) -> MNTM:
        return MNTM(
            states=self.states,
            input_symbols=self.input_symbols,
            tape_symbols=self.tape_symbols,
            n_tapes=self.n_tapes,
            transitions=self.transitions,
            initial_state=self.initial_state,
            blank_symbol=self.blank_symbol,
            final_states=self.final_states
        )
