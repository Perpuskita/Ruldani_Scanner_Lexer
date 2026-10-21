from ruldani_scanner_lexer import reguler_expression
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, print_expression
from ruldani_scanner_lexer import nondeterministic_finite_automata
from ruldani_scanner_lexer.logging import logging
import os

def clear():
    print(f"\nenter untuk melanjutkan..")
    input()
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    # membuat sebuah example untuk regex
    # contoh untuk memindai token float 
    regex_example: str = "float|((1|9).(1|9)*)f"
    
    # membuat logging
    log: logging = logging()

    # membuat ast dari regex 
    regex: reguler_expression = reguler_expression(string_regex=regex_example, log=log)
    ast: expression = regex.make_ast()

    # mencetak regex yang dimasukan
    regex.print_regex()

    # mencetak hasil ast dari regex
    regex.print_ast()

    # membuat NFA dari ast
    nfa: nondeterministic_finite_automata = nondeterministic_finite_automata(ast=ast, log=log)

    # menampilkan hasil dari ast ke NFA

    # manampilkan hasil dari transition tabel NFA




