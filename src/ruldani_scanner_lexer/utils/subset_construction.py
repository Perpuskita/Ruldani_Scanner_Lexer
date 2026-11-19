from ruldani_scanner_lexer.utils.transition_table import table
from ruldani_scanner_lexer.utils.finite_automata_utils.finite_automata import finite_automata
from ruldani_scanner_lexer.utils.transition_table_utils.transition_function import transition_function

class subset_construction:
    def __init__(self, nfa_table: table):
        self.table_nfa: table = nfa_table
        self.table_dfa: table = None

        self.total_state: list[finite_automata] = []
        self.parse_nfa()
        pass
    
    # parse and loop
    def parse_nfa(self) -> table:
        himpunan_input: list[str] = self.table_nfa.himpunan_input
        himpunan_state: list[str] = []
        himpunan_fungsi_transisi: list[transition_function] = self.table_nfa.himpunan_fungsi_transisi


        for state in self.table_nfa.himpunan_state:
            himpunan_state.append(state)

        print(himpunan_input) 
        print(himpunan_state) 
        print("_________ fungsi transisi __________")

        # fungsi transisi 
        for transisi in himpunan_fungsi_transisi:
            print(transisi.get_transition())


        return None

    # death state
    def make_deathstate(self, name: str) -> finite_automata:
        return finite_automata(name=name)

    # measda
    def make_new_state(self, name) -> None:
        self.total_state.append(finite_automata(name=name))
        return None

    
