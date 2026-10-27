from .utils import table 
from .utils.pratt_parser_utils import expression, print_expression
from .utils.finite_automata_utils import finite_automata
from .utils.thompson_construction import thompson_construction
from .logging import logging

class nondeterministic_finite_automata:
    def __init__(self, ast: expression, log: logging = None):
        self.ast = ast
        self.thompson_construction: thompson_construction = thompson_construction(expression_ast=ast)
        self.transition_table: table = self.make_transition_table()

        # membuat kelas logging
        if log is None :
            self.logging: logging = logging()
        else:
            self.logging: logging = log
        self.nfa: list[finite_automata] = []

    def print_ast(self):
        self.logging.print_ast_pratt(ast=self.ast)
        return None

    def print_thompson_construction(self) -> None:
        res: str = self.thompson_construction.print_list_nfa()
        self.logging.print_nondeterministic_finite_automata(res)
        return None

    # membuat transisi tabel yang didapatkan dari self.thompson construction
    def make_transition_table(self)-> table:

        # deklarasi state, input dan start dari node i 
        state: list[str]   = self.thompson_construction.himpunan_state
        input_s: list[str] = self.thompson_construction.himpunan_input
        start   = "q0"

        table_transisi = table(state, input_s, start)
        transisi_table: list[str,str,str] = self.thompson_construction.transisi

        # menambahkan fungsi transisi
        for transisi in transisi_table :
            table_transisi.add_transition(state=transisi[0], input=transisi[1], fungsi_transisi=transisi[2])

        # menambahkan accepting node
        table_transisi.add_accepting_node(node="q2")

        return table_transisi

    def print_transition_table(self):
        self.transition_table.show()
        return None


