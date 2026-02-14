from ruldani_scanner_lexer import reguler_expression

if __name__ == "__main__":
    
    # membuat reguler expression baru
    regex = reguler_expression("a(dc)*")
    hasil = regex.compile(3)

    # menampilkan hasil regex
    print(hasil)