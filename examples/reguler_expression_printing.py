# from reguler_expression import reguler_expression
from ruldani_scanner_lexer import reguler_expression

if __name__ == "__main__":
    regex = reguler_expression("a(dc)*")
    hasil = regex.compile(3)
    print(hasil)