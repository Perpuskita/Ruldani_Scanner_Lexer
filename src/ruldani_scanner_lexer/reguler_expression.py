"""
Reguler expression adalah cara untuk meciptakan pola ekpressi dengan notasi yang diberikan.
Reguler expression pertama kali dikemukakan pada tahun 1950 oleh Stephen Klenee.
Reguler expression merupakan salah satu fondasi dalam teori automata dan komputasi.
"""

from .utils.parser_reguler_expression import lexer_pratt_parsing, pratt_parsing, expression
from .exceptions.error import lexical_error

# urutan prioritas operator
presendace = {
    "|" : 1,
    "*" : 2,
    "-" : 2,
    "^" : 2,
    "?" : 2,
    "[" : 2,
    "]" : 2,
    "(" : 2,
    ")" : 2,

}

# numerik dan angka
numerik = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# mendefinisikan epsilon
epsilon = "ε"

# mendefinisikan class error
EXCEPTION_LEXER = lexical_error()


# class untuk mengolah regular expression
class reguler_expression :

    # inisialisai class
    def __init__(self, string_regex: str):
        # print(string_regex)
        self.string:str = string_regex
    
    # mencetak dari semua hasil dari regex
    def compile(self, jumlah: int = 1) -> list:

        # mengambil lexical dan ast hasil parser pratt parsing
        lexical = lexer_pratt_parsing(self.string)
        parser  = pratt_parsing(lexical)
        ast     = parser.parse_expression()

        render  = self.render(ast, jumlah=jumlah, root=True)
        print(f" hasil regex : {render}")

        # cetak hasil
        return render

    # fungsi yang digunakan untuk melakukan rendering
    def render(self, ast: expression, jumlah: int = 1, root: bool = False) -> list:
        # error jika parameter jumlah di assign kurang dari 2
        if jumlah < 1:
            raise ValueError ("jumlah harus diatas 1 ")

        # mendapatkan operator dari expressi
        op = ast.operator.get_token()
        
        # mendapatkan lhs dari ekspressi
        lhs: list = []

        if type(ast.lhs) == expression :
            lhs = self.render(ast.lhs, jumlah=jumlah)
        else :
            lhs = [ast.lhs.get_token()]

        rhs: list = []
        if type(ast.rhs) == expression :
            rhs = self.render(ast.rhs, jumlah=jumlah)
        else :
            rhs = [ast.rhs.get_token()]

        # menentukan jumlah maximum dari hasil reguler expression yang bisa dirender
        # apabila jumlah melebihi maximum hasil reguler expression maka error
        # print(len(rhs))
        
        maximum_render:int = 0

        if op == "|" :
            maximum_render = len(lhs) + len(rhs) + 1
        
        elif op == "*" :
            maximum_render = 999

        else:
            maximum_render = len(lhs) + len(rhs) - 1

        res: list = [] # hasil berupa list string

        if jumlah > maximum_render and root:
            raise ValueError(EXCEPTION_LEXER.maximum_render_exception())

        # render satu persatu hasil dari operasi
        # algoritma : 
        # ambil lhs char dari lhs[i%lhs.count]  
        # ambil rhs char dari rhs[i%rhs.count]
        # tentukan operasi yang akan dilakukan berikutnya
        # operasi ditentukan dari jenis OP
        # eksekusi dengan operasi yang ditentukan

        jumlah_loop: int = jumlah

        for i in range(jumlah):
            # mendapatkan hasil dari lhs dan rhs ke - i selama loop
            lhs_char = lhs[i % len(lhs)]
            rhs_char = rhs[i % len(rhs)]

            temp: list = []

            # memperoleh hasil operasi
            if op == "+" :
                temp = self.concatination(lhs_char, rhs_char)
            elif op == "|" :
                temp = self.alternation(lhs_char, rhs_char)
            elif op == "*" :
                temp = self.klenee_closure(lhs_char, jumlah=jumlah)

            # kondisional untuk melakukan looping terhadap temp yang sudah dilakukan
            for chars in temp:
                alte_des: bool = False
                for res_c in res:
                    if chars == res_c:
                        alte_des = True
                        continue
                
                if alte_des:
                    continue

                res.append(chars)
                # kondisional yang diperlukan untuk keluar dari loop
                jumlah_loop = jumlah_loop - 1
                if jumlah_loop < 1:
                    print(res)
                    return res
            
        return res

    def eval (self, string_a: str) -> bool:
        return None

    def klenee_closure(self, string_a: str, jumlah: int = 2)-> list:
        
        # return None jika string_a adalah None
        if string_a is None :
            print(EXCEPTION_LEXER.none_variable_klenee_closure_exception())
            return None
        
        if jumlah < 2 :
            print(EXCEPTION_LEXER.minimum_klenee_closure_exception())
            return None

        # menampung result dari klenee closure
        res: list = []
        reps: str = ""

        for i in range(jumlah):
            res.append(reps + string_a)
            reps = res[-1]

        # print(f"hasil dari klenee closure adalah {res}")
        # mengembalikan nilai hasil klenee closure
        return res

    # mencetak hasil dari concatination
    def concatination(self, string_a: str, string_b: str)-> list:
        
        # return None jika kedua string adalah None
        if string_a is None or string_b is None:
            print(EXCEPTION_LEXER.none_variabel_concatination_exception())
            return None
        
        # return string b jika di concate dengan epsilon
        if string_a == epsilon:
            return string_b
        
        if string_b == epsilon:
            return string_a

        # return gabungan dari string a dan string b
        res = [string_a + string_b]
        # print(f"hasil dari concatination adalah : {res}")
        
        # mengembalikan nilai dari hasil concatination
        return res

    # mencetak hasil dari alternation
    def alternation(self, string_a: str, string_b: int)-> list:

        # return none jika salah satu string adalah none
        if string_a is None or string_b is None:
            print(EXCEPTION_LEXER.none_variabel_alternation_exception())
            return None
        
        # menampung hasil dari alternation
        res = []
     
        res.append(string_a)
        res.append(string_b)

        # menambahkan epsilon pada hasil alternation
        res.append(epsilon)
        # print(f"hasil dari alternation adalah{res}")

        # mengembalikan nilai dari harsil alternation
        return res


if __name__ == "__main__":
    re = reguler_expression("ab")
    print(re.compile() == ['ab']) 