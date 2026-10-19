from ruldani_scanner_lexer import reguler_expression
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, print_expression

if __name__ == "__main__":

    # membuat sebuah example untuk regex
    regex_example: str = "def|fn*"

    # membuat sebuah printer untuk ast
    printer: print_expression = print_expression()

    # membuat ast dari regex 
    regex: reguler_expression = reguler_expression(string_regex=regex_example)
    ast: expression = regex.make_ast()
    hasil: str = printer.print_expression(ast=ast)

    # melakukan print ast dalam bentuk string
    # nanti dah dibenerin hasilnya, capek kali bikin tree di terminal
    print(hasil)




