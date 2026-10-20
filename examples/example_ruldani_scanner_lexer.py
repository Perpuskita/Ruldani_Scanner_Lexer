from ruldani_scanner_lexer import reguler_expression
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, print_expression
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
    # regex_example: str = "fl(oa)t"
    print(f"\ncontoh regex adalah :\n'{regex_example}'")
    clear()

    # membuat sebuah printer untuk ast
    printer: print_expression = print_expression()

    # membuat ast dari regex 
    regex: reguler_expression = reguler_expression(string_regex=regex_example)
    ast: expression = regex.make_ast()
    hasil: str = printer.print_expression(ast=ast)

    # menampilkan hasil ast dalam bentuk string
    # nanti dah dibenerin hasilnya, capek kali bikin tree di terminal
    print(f"\nmenguraikan hasil ast dari regex dengan menggunakan pratt parsing : \n\n{hasil}")
    clear()

    # membuat NFA dari ast

    # menampilkan hasil dari ast ke NFA

    # manampilkan hasil dari transition tabel NFA




