from ruldani_scanner_lexer import reguler_expression

if __name__ == "__main__":
    regex = reguler_expression("def|func|class|if|else|return|int|float")
    hasil = regex.compile(8)
    print(hasil)