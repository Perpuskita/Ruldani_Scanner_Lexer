from ruldani_scanner_lexer.utils.thompson_construction_utils import klenee_closure_thompson

if __name__ == "__main__" :
    conversion: klenee_closure_thompson = klenee_closure_thompson()
    conversion.make_finite_automata(str_a = "a")