from ruldani_scanner_lexer.utils.pratt_parser_utils.type_token import ID, OP, EOF
from ruldani_scanner_lexer.utils.pratt_parser_utils.token import token
from ruldani_scanner_lexer.utils.pratt_parser_utils.binding_power import BINDING_POWER

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

            if BINDING_POWER.get(char,0) != 0:
                # print(f"append token {char} dengan tipe {op}")
                new = token(char,OP)
                res.append(new)
            else:
                # print(f"append token {char} dengan tipe {atom}")
                new = token(char,ID)
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
            return token(EOF, EOF)
