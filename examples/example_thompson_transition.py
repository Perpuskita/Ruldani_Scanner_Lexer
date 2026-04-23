from ruldani_scanner_lexer.utils import pratt_parsing, thompson_construction
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata

if __name__ == "__main__" :
    tesregex : str = "oo|po"
    pratt : pratt_parsing = pratt_parsing(tesregex)
    asts : expression = pratt.parse_expression() 
    thompson: thompson_construction = thompson_construction(asts)
    tes : list [finite_automata] = thompson.listing

    thompson.print_listing(tes[0])

    