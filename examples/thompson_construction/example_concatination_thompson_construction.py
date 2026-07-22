from ruldani_scanner_lexer.utils.thompson_construction_utils.concatination_thompson import concatination_thompson
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata

if __name__ == "__main__" :
    converter: concatination_thompson = concatination_thompson()
    result: list[finite_automata] = converter.make_finite_automata(str_a = "a", str_b = "b")
    converter.print_finite_automata(result)