from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata
from ruldani_scanner_lexer.utils.transition_table import table
from ruldani_scanner_lexer.utils.finite_automata_utils import *
from ruldani_scanner_lexer.logging import logging

"""
Deterministic finite automata adalah jenis finite automata yang ciri khasnya
setiap input alphabet/simbol dari suatu state hanya akan bertransisi ke satu state lain.
dengan kata lain deterministik tidak ambigu dalam menentukan next state
"""
class deterministic_finite_automata:
    def __init__(self, table:table, log: logging = None):
        self.table: table = table

        # make logging
        if log == None:
            self.log = logging()
        else:
            self.log: logging = log

    def make_dfa(self) -> list[finite_automata]:
        return None

    def print_subset_construction(self)->None:
        return None

    def print_transition_table(self) -> None:
        self.log.print_table_transition(    himpunan_state=self.table.himpunan_state, 
                                            himpunan_input=self.table.himpunan_input,
                                            himpunan_fungsi_transisi=self.table.himpunan_fungsi_transisi,
                                            himpunan_accepting_state=self.table.himpunan_accepting_state,
                                            start_state=self.table.start_state)
        return None
    
    def print_dfa(self) -> None:
        return None