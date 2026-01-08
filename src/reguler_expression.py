"""
Reguler expression adalah cara untuk meciptakan pola ekpressi dengan notasi yang diberikan.
Reguler expression pertama kali dikemukakan pada tahun 1950 oleh Stephen Klenee.
Reguler expression merupakan salah satu fondasi dalam teori automata dan computasi.
"""

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

# class untuk mengolah regular expression
class reguler_expression :

    # inisialisai class
    def __init__(self, string_regex: str):
        # print(string_regex)
        self.string = string_regex
    
    # mencetak dari semua hasil dari regex
    def leaguage_of_s(self):
        result = self.string
        
        return result

    def klenee_closure(self, string_a: str, jumlah: int = 2):
        
        # return None jika string_a adalah None
        if string_a is None :
            print("klenee closure not valid")
        
        if jumlah < 2 :
            print("klenee closure kuranf dari 2 sehingga tidak valid ")

        # menampung result dari klenee closure
        res = []
        
        for i in range(jumlah):
            res.append(string_a)

        print(f"hasil dari klenee closure adalah {res}")
        # mengembalikan nilai hasil klenee closure
        return res

    # mencetak hasil dari concatination
    def concatination(self, string_a: str, string_b: str)-> str:
        
        # return None jika kedua string adalah None
        if string_a is None or string_b is None:
            print("concatination not valid")
            return None
        
        # return gabungan dari string a dan string b
        res = string_a + string_b
        print(f"hasil dari concatination adalah : {res}")
        
        # mengembalikan nilai dari hasil concatination
        return res

    # mencetak hasil dari alternation
    def alternation(self, string_a: str, string_b: int):

        # return none jika salah satu string adalah none
        if string_a is None or string_b is None:
            print("alternation not valid")
            return None

        # menampung hasil dari alternation
        res = [string_a, string_b, ""]
        print(f"hasil dari alternation adalah{res}")

        # mengembalikan nilai dari harsil alternation
        return res
    
    # mengambil nilai dari alphabet
    def range_character(self, string_a: str, string_b: str):
        
        # return none jika salah satu string adalah none
        if string_a is None or string_b is None:
            print("range character not valid")
            return None
        
        # penampung hasil dari range character
        res: list = []
        les: bool = False
        
        # looping untuk memperoleh string awal dan akhir 
        for i in alphabet:
            # mencari string awal
            if i == string_a:
                les = True

            # mencari string akhir
            if i == string_b:
                break
            
            # menambahkan alphabet ketika les = true
            if les :
                res.append(i)
                
        return res

# testing untuk class reguler expression
if __name__ == "__main__":
    
    # testing regex
    re = reguler_expression("a|b")
    re.leaguage_of_s()

    # testing concatination
    re.concatination("n","s")
    re.concatination(None, "t")
    re.concatination("t", None )
    
    # testing klenee_closure
    re.klenee_closure("r")
    re.klenee_closure("r", 5)
    re.klenee_closure(None)

    # testinf alternation
    re.alternation("n", "s")
    re.alternation(None, "s")
    re.alternation("n", None)

