from ruldani_scanner_lexer.utils.pratt_parser_utils.expression import expression

class print_expression:
    def __init__ (self):
        pass

    def print_expression(self, ast:expression) -> str :
        OP = ast.operator.get_token()
        lhs = ast.lhs

        if type(lhs) == expression :
            lhs = self.print_expression(lhs)
        else :
            lhs = lhs.get_token()

        rhs = ast.rhs
        if type(rhs) == expression :
            rhs = self.print_expression(rhs)
        else :
            rhs = rhs.get_token()
        
        res = f"({lhs + OP + rhs})"
        return res
