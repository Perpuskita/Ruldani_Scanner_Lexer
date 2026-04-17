from ruldani_scanner_lexer import reguler_expression


if __name__ == "__main__":
    re: reguler_expression = reguler_expression("")
    
    # concationation regex
    concatination: list[str] = re.concatination("lexer", "foo")

    # alternation regex
    alternation: list[str] = re.alternation("scanner", "lexer")

    # klenee closure regex
    klenee_closure: list[str] = re.klenee_closure("wello", 3)

    
    # print hasil
    print(concatination)
    print(alternation)
    print(klenee_closure)