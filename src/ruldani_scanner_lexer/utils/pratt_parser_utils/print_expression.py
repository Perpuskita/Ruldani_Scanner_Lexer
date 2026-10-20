from ruldani_scanner_lexer.utils.pratt_parser_utils.expression import expression
from ruldani_scanner_lexer.constant import KLENEE_CLOSURE, CONCATINATION, ALTERNATION
from ruldani_scanner_lexer.constant import CHILD,LAST_CHILD,CHILD_PREFIX,ROOT_PREFIX

class print_expression:
    def __init__ (self):
        pass

    def print_expression(self, ast:expression, prefix: str=ROOT_PREFIX) -> str :

        OP = ast.operator.get_token()
        if OP == CONCATINATION:
            OP = "con+"
        
        elif OP == ALTERNATION:
            OP = "alt-"
        
        elif OP == KLENEE_CLOSURE:
            OP = "kc*"

        if prefix == ROOT_PREFIX:
            OP = f"{prefix}{OP}"
        

        lhs = ast.lhs

        if type(lhs) == expression :
            lhs = self.print_expression(lhs, prefix=prefix+CHILD_PREFIX)
        else :
            lhs = lhs.get_token()

        rhs = ast.rhs
        if type(rhs) == expression :
            rhs = self.print_expression(rhs, prefix=prefix+CHILD_PREFIX)
        else :
            rhs = rhs.get_token()
        
        rhs = f"{prefix + LAST_CHILD + rhs}"
        lhs = f"{prefix + CHILD + lhs}"

        res = f"{OP}\n{lhs}\n{prefix}{CHILD_PREFIX}\n{rhs}"
        return res