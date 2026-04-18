from ruldani_scanner_lexer.utils.pratt_parser_utils import token, lexer_pratt_parsing, expression
from ruldani_scanner_lexer.utils.pratt_parser_utils import OP, ID, EOF, BINDING_POWER

# class utama untuk melakukan parsing
class pratt_parsing:
    def __init__(self, lexer: lexer_pratt_parsing):
        self.lexer = lexer

    def binding_power(self, operator: str):
        bp = BINDING_POWER.get(operator)
        return bp

    def parse_expression(self, min_bp=0):
        
        # mengambil token untuk lhs
        lhs = self.lexer.next_token()
        if lhs.get_token() == "(":
            lhs = self.parse_expression()
            if self.lexer.next_token().get_token() != ")":
                raise ValueError ("close bracket not found")
        
        elif lhs.get_token() == "[":
            lhs = self.parse_expression()
            if self.lexer.next_token().get_token() != "]":
                raise ValueError ("close bracket not found")

        elif lhs.get_token() == "*":
            return token("*", OP)

        elif lhs.get_type() != ID :
            raise ValueError ("tipe lhs not valid")

        while True:
            # melihat token untuk operator
            operator = self.lexer.peek_token()
            conc : bool = False

            # break jika token EOF atau token berakhir
            if operator.get_type() == EOF:
                break
            elif operator.get_token() == ")":
                break
            elif operator.get_token() == "]":
                break
            elif operator.get_token() == "*":
                conc = True
            elif operator.get_type() == ID:
                operator = token("+", OP)
                conc = True

            elif operator.get_type() != OP:
                raise ValueError("tipe token tidak valid")
            
            # menetukan left binding power dari token OP

            lbp = self.binding_power(operator.get_token())
            rbp = lbp+0.1 

            # konsisi untuk membandingkan token operator dengan operator sebelumnya
            if lbp < min_bp :
                break
            
            if not conc :
                self.lexer.next_token()

            rhs = self.parse_expression(rbp)
            lhs = expression(operator, lhs, rhs)

        # mengembalikan lhs yang sementara ini bisa berupa token maupun ekspressi
        return lhs

    def print_token(self, ast: expression):

        OP = ast.operator.get_token()
        lhs = ast.lhs

        if type(lhs) == expression :
            lhs = self.print_token(lhs)
        else :
            lhs = lhs.get_token()

        rhs = ast.rhs
        if type(rhs) == expression :
            rhs = self.print_token(rhs)
        else :
            rhs = rhs.get_token()
        
        res = f"({lhs + OP + rhs})"
        return res

    def get_ast(self):
        return self.ast
