binding_power = {
    "|" : 1.0,
    "+" : 2.0,  # operator for concatination
    "*" : 3.0   # operator for klenee closure
}

# name token
op = "operator" 
atom = "atom"
eof = "eof"

# class token lexical analysis
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
            if char == " ":
                continue

            if binding_power.get(char,0) != 0:
                # print(f"append token {char} dengan tipe {op}")
                new = token(char,op)
                res.append(new)
            else:
                # print(f"append token {char} dengan tipe {atom}")
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

# class untuk menampung ekpressi
class expression:
    def __init__(self, operator_token = None, 
                 lhs_expression = None,  
                 rhs_expression = None ):
        
        self.operator: token = operator_token
        self.lhs: token = lhs_expression
        self.rhs: token = rhs_expression

# class utama untuk melakukan parsing
class pratt_parsing:
    def __init__(self, lexer: lexer_pratt_parsing):
        self.lexer = lexer

    def binding_power(self, operator: str):
        bp = binding_power.get(operator)
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
            return token("*", op)

        elif lhs.get_type() != atom :
            raise ValueError ("tipe lhs not valid")

        while True:
            # melihat token untuk operator
            operator = self.lexer.peek_token()
            conc : bool = False

            # break jika token eof atau token berakhir
            if operator.get_type() == eof:
                break
            elif operator.get_token() == ")":
                break
            elif operator.get_token() == "]":
                break
            elif operator.get_token() == "*":
                conc = True
            elif operator.get_type() == atom:
                operator = token("+", op)
                conc = True

            elif operator.get_type() != op:
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
        return res

    def get_ast(self):
        return self.ast



if __name__ == "__main__":
    test = "a|bcd*d"
    lexical = lexer_pratt_parsing(test)
    # lexical.print_tokens()

    pratt = pratt_parsing(lexical)
    ast = pratt.parse_expression()
    result = pratt.print_token(ast)
    print(result)