from ruldani_scanner_lexer.utils.finite_automata import finite_automata

class thompson_constraction_abstract :
    def __init__(self):
        pass

    def print_finite_automata( self, node_finite_automata: finite_automata ):
        '''
        fungsi ini digunakan untuk mencetak finite automata dalam console
        contoh hasil cetak dari finite automata, q1 = a
        '''
        for node in node_finite_automata.next :
            print(f"q{node_finite_automata.name} -> q{node.next_node.name} = {node.edge}")
        
        return None