class finite_automata_node:
    def __init__(self, string_a):
        print("inisialisasi finite automata node berhasil")
        self.expression = None
        self.next = []
    
    def print_node(self):
        return None

    def next_node(self, node_s: finite_automata_node):
        self.next.append(node_s)
        return None

class accepting_node:
    def __init__(self) :
        print("inisialisasi accepting node berhasil")
