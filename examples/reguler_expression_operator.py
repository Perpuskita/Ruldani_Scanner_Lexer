from ruldani_scanner_lexer import ruldani_scanner_lexer

re = ruldani_scanner_lexer("")
klenee_closure = re.klenee_closure("wello", 3)
alternation = re.alternation("scanner", "lexer")
concatination = re.concatination("lexer", "foo") 