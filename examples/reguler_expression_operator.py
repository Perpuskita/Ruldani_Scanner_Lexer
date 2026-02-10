from ruldani_scanner_lexer import reguler_expression


if __name__ == "__main__":
    re = reguler_expression("")

    klenee_closure = re.klenee_closure("wello", 3)
    alternation = re.alternation("scanner", "lexer")
    concatination = re.concatination("lexer", "foo")

    # print
    print(klenee_closure)
    print(alternation)
    print(concatination)