from ruldani_scanner_lexer.utils.pratt_parser_utils.token import token

# class untuk menampung ekpressi
class expression:
    def __init__(self, operator_token = None, 
                 lhs_expression = None,  
                 rhs_expression = None ):
        
        self.operator: token = operator_token
        self.lhs: token = lhs_expression
        self.rhs: token = rhs_expression