from ruldani_scanner_lexer.utils.thompson_construction_utils.concatination_thompson import concatination_thompson

if __name__ == "__main__" :
    conversion: concatination_thompson = concatination_thompson()
    conversion.make_finite_automata(str_a = "a", str_b = "b")