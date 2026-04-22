from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata

class thompson_constraction_abstract :
    def __init__(self):
        pass

    def print_finite_automata( self, node_finite_automata: list[finite_automata] ):
        '''
        fungsi ini digunakan untuk mencetak finite automata dalam console
        contoh hasil cetak dari finite automata, q1 = a
        '''
        for nodes in node_finite_automata:
            for node in nodes.next :
                print(f"q{nodes.name} -> q{node.next_node.name} = {node.edge}")
        
        return None