from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata
from ruldani_scanner_lexer.utils.thompson_construction_utils.result_thompson import print_thompson

class thompson_constraction_abstract :
    def __init__(self):
        pass

    def print_finite_automata( self, node_finite_automata: list[finite_automata] ) -> None:
        '''
        fungsi ini digunakan untuk mencetak finite automata dalam console
        contoh hasil cetak dari finite automata, q1 = a
        '''

        temp: print_thompson = print_thompson(node_finite_automata)
        hasil: tuple = temp.print_thompson()
        
        for node in hasil :
            print(node)

        return None
