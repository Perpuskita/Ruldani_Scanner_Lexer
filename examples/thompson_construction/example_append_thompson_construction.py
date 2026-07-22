from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata
from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson, concatination_thompson, klenee_closure_thompson, result_thompson, append_thompson
from ruldani_scanner_lexer.constant import EPSILON

if __name__ == '__main__':
    
    # make class
    converter_alternation: alternation_thompson = alternation_thompson()
    converter_concationation: concatination_thompson = alternation_thompson()

    # make example
    example_alternation: list[finite_automata] = converter_alternation.make_finite_automata(EPSILON, EPSILON)
    example_concationation: list[finite_automata] = converter_concationation.make_finite_automata("a", "b")

    # result
    append: result_thompson = append_thompson()
    hasil: list[finite_automata] = append.append_on_alternation(root=example_alternation, param_a=example_concationation)
    
    # print
    converter_alternation.print_finite_automata(hasil)

