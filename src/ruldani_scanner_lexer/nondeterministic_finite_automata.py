from .utils import table 
from .utils.pratt_parser_utils.expression import expression
from .utils.finite_automata_utils import finite_automata

class nondeterministic_finite_automata:
    def __init__(self, ast: expression):
        self.ast = ast

    def print_ast(self):
        return None

    def make_thompson_construction(self) -> list[finite_automata]:
        return None

    def print_thompson_construction(self):
        return None

    def make_transition_table(self) :
        return None

    def print_transition_table(self):
        return None

if __name__ == "__main__" :
    nfa = nondeterministic_finite_automata()
    nfa.add_node()
