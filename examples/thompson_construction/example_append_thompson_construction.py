from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata
from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson, concatination_thompson, klenee_closure_thompson, result_thompson, append_thompson
from ruldani_scanner_lexer.constant import EPSILON

if __name__ == '__main__':
    
    # make class
    converter_alternation: alternation_thompson = alternation_thompson()
    converter_concationation: concatination_thompson = concatination_thompson()

    # make example
    root: list[finite_automata] = converter_alternation.make_finite_automata(EPSILON, EPSILON)
    param_a: list[finite_automata] = converter_concationation.make_finite_automata("a", "b")
    param_b: list[finite_automata] = converter_alternation.make_finite_automata("c", "d")

    # result
    append: append_thompson = append_thompson()
    hasil: list[finite_automata] = append.append_on_alternation(root=root, param_a=param_a, param_b=param_b)
    
    # print
    converter_alternation.print_finite_automata(hasil)

