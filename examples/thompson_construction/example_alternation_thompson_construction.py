from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson

if __name__ == "__main__" :
    conversion: alternation_thompson = alternation_thompson()
    conversion.make_finite_automata(str_a = "a", str_b = "b")