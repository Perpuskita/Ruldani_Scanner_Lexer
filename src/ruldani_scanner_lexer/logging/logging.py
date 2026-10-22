import os
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, print_expression
from ruldani_scanner_lexer.constant import GREETINGS
from ruldani_scanner_lexer.utils.transition_table import terminal_table_transition

class logging:
    def __init__(self):
        self.print_pratt : print_expression = print_expression()
        self.print_table : terminal_table_transition = terminal_table_transition()

    def greeting(self):
        print(GREETINGS)
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
        print(f"note:\n- con+ = concatination\n- alt- = alternation\n- kc*  = klenee closure\n- abaikan * pada hasil kc")
        self.clear_screen()
        return None

    # mencetak hasil dari konversi ast regex ke nfa
    # nfa yang dihasilkan oleh thompson construction
    def print_nondeterministic_finite_automata(self)-> None:
        return None 

    # mencetak tabel transisi yang digunakan
    def print_table_transition(self, 
              himpunan_state: list, 
              himpunan_input: list,
              himpunan_fungsi_transisi: list,
              himpunan_accepting_state: list,
              start_state: str ) -> None:

        transition_str  : list[list[str]] =  []
        for fungsi_transisi in himpunan_fungsi_transisi :
            transition_str.append(fungsi_transisi.get_transition())

        show_terminal   : str = self.print_table.desc(  himpunan_state = himpunan_state, 
                                                        himpunan_input = himpunan_input, 
                                                        himpunan_fungsi_transisi = transition_str,
                                                        himpunan_accepting_state = himpunan_accepting_state,
                                                        start_state= start_state)
        print(show_terminal)
        return None