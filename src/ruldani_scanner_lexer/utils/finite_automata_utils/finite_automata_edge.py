EPSILON = "Ɛ"

class finite_automata_edge:
    """
    finite auromata arrow edge digunakan untuk menunjuk state berikutnya. Finite automata edge dapat berisi beberapa method
    """
    def __init__(self, next_node, edge: str = EPSILON):
        self.next_node = next_node
        self.edge: str = edge

    def evaluate(self, string_a: str) -> bool:
        if self.edge == string_a:
            return True
        
        return False
    
    def next_finite_automata(self) :
        return self.next_node