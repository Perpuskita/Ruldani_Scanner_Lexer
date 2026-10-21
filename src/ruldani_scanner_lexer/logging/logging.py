import os
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, print_expression
from ruldani_scanner_lexer.constant import GREETINGS

class logging:
    def __init__(self):
        print(GREETINGS)
        self.print_pratt : print_expression = print_expression()
        self.clear_screen()

    def clear_screen(self) -> None:
        print(f"\nenter untuk melanjutkan..")
        input()
        os.system("cls" if os.name == "nt" else "clear")

    def print_regex(self, regex: str):
        print(f"\nregex yang dimasukan adalah :\n'{regex}'")
        self.clear_screen()

    # mecetak hasil abstract sytax tree
    # ast yang dihasilkan pratt parsing
    def print_ast_pratt(self, ast: expression) -> None:
        hasil: str = self.print_pratt.print_expression(ast=ast)        
        
        print(f"\nmenguraikan hasil ast dari regex dengan menggunakan pratt parsing : \n\n{hasil}\n")
        print(f"note:\n- con+ = concatination\n- alt- = alternation\n- kc*  = klenee closure")
        self.clear_screen()
        return None

    # mencetak hasil dari konversi ast regex ke nfa
    # nfa yang dihasilkan oleh thompson construction
    def print_nondeterministic_finite_automata(self)-> None:
        return None 

    def print_nfa_transition_table(self) -> None:
        return None