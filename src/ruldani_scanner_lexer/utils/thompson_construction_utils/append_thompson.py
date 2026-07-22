from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge

class append_thompson():
    def __init__(self):
        pass

    def append_on_alternation(  self, root: list[finite_automata], 
                                param_a: list[finite_automata] = [],
                                param_b: list[finite_automata] = [] ) -> list[finite_automata]:
        
        # mengembalikan nilai jika kedua parameter adalah NONE
        if len(param_a) == 0 and len(param_b) == 0:
            return None
        
        if root == None :
            return None
        
        # mengambil finite automata dari root 
        root_a: finite_automata_edge = root[2].next[0]
        root_b: finite_automata_edge = root[4].next[0]


        # kondisi jika param a diberikan
        if len(param_a) > 0:
            # menyimpan tail keadalam variabel sementara
            tail: finite_automata = root_a.next_finite_automata()

            # set next finite automata ke param a[0]
            root_a.set_finite_automata(param_a[0])

            # set param a terakhir menjadi tail
            param_a[-1].next_node(tail)

        # kondisi jika param a diberikan
        if len(param_b) > 0:
            # menyimpan tail keadalam variabel sementara
            tail: finite_automata = root_b.next_finite_automata()

            # set next finite automata ke param a[0]
            root_b.set_finite_automata(param_b[0])

            # set param a terakhir menjadi tail
            param_b[-1].next_node(tail)

        return root
