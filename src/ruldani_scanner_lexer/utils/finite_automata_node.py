"""
finite automata node berisi node 
"""

class finite_automata_node:
    """
    finite automata node merupakan sebuah node yang berisi state 
    pada finite automata. Finite automata dilambangkan dengan lingkaran.
    node atau state ini memiliki sejumlah transisi yang dilambangkan dengan panah.
    """
    def __init__(self, string_a):
        print("inisialisasi finite automata node berhasil")
        self.expression = None
        self.next = None
    
    def print_node(self):
        return None

    def next_node(self, node_s: finite_automata_node):
        self.next.append(node_s)
        return None

class accepting_node:
    """
    accepting node merupakan sebuah state yang dilambangkan dengan lingkaran ganda.
    state ini biasanya berada diakhir barisan node finite automata.
    """
    def __init__(self) :
        print("inisialisasi accepting node berhasil")


class finite_automata_arrow:
    """
    finite auromata arrow merupakan sebuah diantara state. finite automata ini dapat
    menunjuk dirinya sendiri.
    """
    def __init__(self):
        pass