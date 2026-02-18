"""
finite automata node berisi node - node untuk melambangkan finite automata
finite automata ini merupakan translasi dari transition table
"""

class finite_automata_node:
    """
    finite automata node merupakan sebuah node yang berisi state 
    pada finite automata. Finite automata dilambangkan dengan lingkaran.
    node atau state ini memiliki sejumlah transisi yang dilambangkan dengan panah.
    """
    def __init__(self,  nama_node: str ):
        # print("inisialisasi finite automata node berhasil")
        self.nama = nama_node

    def get_node(self):
        return self.nama

class accepting_node:
    """
    accepting node merupakan sebuah state yang dilambangkan dengan lingkaran ganda.
    state ini biasanya berada diakhir barisan node finite automata.
    """
    def __init__(self, node: finite_automata_node) :
        self.node = node
        pass

    def get_node(self):
        return self.node


class finite_automata_edge:
    """
    finite auromata arrow merupakan sebuah diantara state. finite automata ini dapat
    menunjuk dirinya sendiri.
    """
    def __init__(self, nodea: finite_automata_node, nodeb: finite_automata_node ):
        pass


if __name__ == "__main__" :
    finite_automata_node("foo").get_node()

    print("foo" == "foo")