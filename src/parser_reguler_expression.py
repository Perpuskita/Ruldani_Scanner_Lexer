binding_power = {
    "+" : 1.0,
    "-" : 1.0,
    "*" : 2.0,
    "/" : 2.0,
}

op = "operation"
atom = "atom"
eof = "eof"

# class token
class token:
    def __init__(self, char, type_token):
        self.char = char
        self.type_token = type_token

    def print_token(self):
        print(f"token {self.char} ")

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

# class operation
class ast_pratt:
    def __init__(self, operator: token, expression: list):
        self.operator = operator
        self.expression = expression

# class utama untuk melakukan parsing
class pratt_parsing:
    def __init__(self, lexer: lexer_pratt_parsing):
        self.lexer = lexer

    def parse_expression(self, min_bp=0):
        
        # menentukan lhs
        lhs = self.lexer.next_token()

        if lhs.type_token == atom:
            print(f"lhs saat ini = {lhs.char}")
        else:
            raise ValueError(f"bad token lhs = {lhs.char}, {lhs.type_token}")
        
        while True :

            # menentukan operator
            operator = self.lexer.peek_token()
            if operator.type_token == eof:
                print(f"token eof break dari loop")
                break
            elif operator.type_token == op:
                print(f"token op saat ini adalah {operator.char}")
            else :
                raise ValueError(f"bad token {operator.char}")

            # menentukan binding power
            l_bp = binding_power.get(operator.char)
            r_bp = l_bp + 0.1
                        
            if l_bp < min_bp:
                break
            
            self.lexer.next_token()

            rhs = self.parse_expression(r_bp)
            lhs = ast_pratt(operator, [lhs, rhs])

        # menyimpan ekpressi kedalam ast
        return lhs

    def print_ast (self, ast : ast_pratt):
        return None


if __name__ == "__main__":
    test = "a+b*y+u/i"
    lexical = lexer_pratt_parsing(test)
    lexical.print_tokens()
    pratt = pratt_parsing(lexical)
    ast = pratt.parse_expression()
    pratt.print_ast(ast)
