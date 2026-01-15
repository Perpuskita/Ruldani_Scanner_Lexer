binding_power = {
    "+" : 1.0,
    "-" : 1.0,
    "*" : 2.0,
    "/" : 2.0,
}

binding_power_regex = {
    "|" : 1.0,
    "c" : 2.0,
    "*" : 3.0,
    "(" : 2.0,
}

op = "operator"
atom = "atom"
eof = "eof"

# class token
class token:
    def __init__(self, char, type_token):
        self.char = char
        self.type_token = type_token
        self.expression = None

    def get_token(self) -> str:
        return self.char
    
    def get_type(self) -> str:
        return self.type_token
    
    
# class pratt parsing
class lexer_pratt_parsing:
    def __init__(self, strings: str):
        self.strings = strings
        self.tokens:list = self.token_generator()

    # memecah string panjang menjadi token
    def token_generator(self) -> list:
        res = []

        # loop untuk membuat token dan jenisnya
        for char in self.strings:
            if binding_power.get(char,0) != 0:
                print(f"append token {char} dengan tipe {op}")
                new = token(char,op)
                res.append(new)
            else:
                print(f"append token {char} dengan tipe {atom}")
                new = token(char,atom)
                res.append(new)
        
        # tambahkan reverse list
        res.reverse()
        return res
    
    # mencetak setiap token dalam analisis lexical
    def print_tokens(self) -> None:
        for token_lexical in self.tokens:
            print(f"token : {token_lexical.char}, type {token_lexical.type_token}")

    # mengambil token dengan menghapus token di tumpukan tertinggi
    def next_token(self) -> token:
        return self.tokens.pop() 
    
    # mengambil token tanpa mengahapus token di tumpukan teratas
    def peek_token(self) -> token:
        if len(self.tokens) > 0:
            return self.tokens[-1]
        else :
            return token(eof, eof)

# class operation
class expression:
    def __init__(self, operator_token = None, 
                 lhs_expression = None,  
                 rhs_expression = None ):
        
        self.operator: token = operator_token
        self.lhs: token = lhs_expression
        self.rhs: token = rhs_expression

    def print_operator(self):
        print(f"operator pada ast pratt ini adalah {self.operator.get_type()}")

    def print_lhs(self):
        print(f"lhs saat ini adalah {self.lhs}")

    def print_rhs(self):
        print(f"lhs saat ini adalah {self.rhs}")


# class utama untuk melakukan parsing
class pratt_parsing:
    def __init__(self, lexer: lexer_pratt_parsing):
        self.lexer = lexer

    def binding_power(self, operator: str):
        bp = binding_power.get(operator)
        return bp

    def parse_expression(self, min_bp=0):
        
        lhs = self.lexer.next_token()
        if lhs.get_token() == "(":
            lhs = self.parse_expression()
            if self.lexer.next_token().get_token() != ")":
                raise ValueError ("close bracket not found")

        elif lhs.get_type() != atom :
            raise ValueError ("lhs not valid")

        while True:
            operator = self.lexer.peek_token()
            if operator.get_type() == eof:
                break
            elif operator.get_token() == ")":
                break
                
            elif operator.get_type() != op:
                raise ValueError("tipe token tidak valid")
            
            lbp = self.binding_power(operator.get_token())
            rbp = lbp+0.1

            if lbp < min_bp :
                break

            self.lexer.next_token()

            rhs = self.parse_expression(rbp)
            lhs = expression(operator, lhs, rhs)

        return lhs

    def print_token(self, ast: expression):

        op = ast.operator.get_token()
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
        
        res = f"({lhs + op + rhs})"
        print(res)

        return res




if __name__ == "__main__":
    test = "(a+b)-c*c/y"
    lexical = lexer_pratt_parsing(test)
    # lexical.print_tokens()

    pratt = pratt_parsing(lexical)
    ast = pratt.parse_expression()
    pratt.print_token(ast)