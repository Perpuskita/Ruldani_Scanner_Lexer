
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