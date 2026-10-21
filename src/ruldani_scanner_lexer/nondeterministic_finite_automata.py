from .utils import table 
from .utils.pratt_parser_utils import expression, print_expression
from .utils.finite_automata_utils import finite_automata
from .logging import logging

class nondeterministic_finite_automata:
    def __init__(self, ast: expression, log: logging = None):
        self.ast = ast
        
        # membuat kelas logging
        if log is None :
            self.logging: logging = logging()
        else:
            self.logging: logging = log


    def print_ast(self):
        self.logging.print_ast_pratt(ast=self.ast)
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
