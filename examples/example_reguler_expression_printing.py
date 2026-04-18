from ruldani_scanner_lexer import reguler_expression

if __name__ == "__main__":
    regex = reguler_expression("a|(dc)|v*")
    hasil = regex.compile(4)
    print(hasil)