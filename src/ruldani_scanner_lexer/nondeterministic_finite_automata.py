from finite_automata_node import finite_automata_node, accepting_node

class nondeterministic_finite_automata:
    def __init__(self):
        self.node = finite_automata_node()
        self.root = self.node

    def add_node(self, string_a: str):   
        node = finite_automata_node(string_a=string_a)
        self.node
        return None

    def end_node(self, string_a: str):
        return None
 
    def print(self):
        for nama_node in self.node:
            print(nama_node)

if __name__ == "__main__" :
    
    nfa = nondeterministic_finite_automata()
    nfa.add_node()
