class finite_automata:
    """
    finite automata node merupakan sebuah node yang berisi state 
    pada finite automata. Finite automata dilambangkan dengan lingkaran.
    node atau state ini memiliki sejumlah transisi yang dilambangkan dengan panah.
    """
    def __init__(self,  nama_node: str, 
                        transisi: list,
                         ):
        
        print("inisialisasi finite automata node berhasil")
        self.expression = None
        self.next = None
    
    def compile_transisi(self):
        return None

    def print_node(self):
        return None

    def next_node(self, node_s):
        self.next.append(node_s)
        return None
