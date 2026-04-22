from ruldani_scanner_lexer.utils import pratt_parsing, thompson_construction
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression

if __name__ == "__main__" :
    tesregex : str = "cow|cato"
    pratt : pratt_parsing = pratt_parsing(tesregex)
    asts : expression = pratt.parse_expression() 
    thompson: thompson_construction = thompson_construction(asts)