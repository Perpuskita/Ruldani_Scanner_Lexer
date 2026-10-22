from .utils import table 
from .utils.pratt_parser_utils import expression, print_expression
from .utils.finite_automata_utils import finite_automata
from .utils.thompson_construction import thompson_construction
from .logging import logging

class nondeterministic_finite_automata:
    def __init__(self, ast: expression, log: logging = None):
        self.ast = ast
        self.thompson_construction: thompson_construction = thompson_construction(expression_ast=ast)

        # membuat kelas logging
        if log is None :
            self.logging: logging = logging()
        else:
            self.logging: logging = log


    def print_ast(self):
        self.logging.print_ast_pratt(ast=self.ast)
        return None

    def make_thompson_construction(self) -> list[finite_automata]:
        self.thompson_construction.read_expression(expression_ast=self.ast)
        return None

    def print_thompson_construction(self):
        self.thompson_construction.print_listing()
        return None

    def make_transition_table(self) :
        return None

    def print_transition_table(self):
        return None


