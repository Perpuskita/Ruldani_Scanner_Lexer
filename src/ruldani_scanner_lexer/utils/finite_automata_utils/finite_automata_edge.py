EPSILON = "Ɛ"

class finite_automata_edge:
    """
    finite auromata arrow edge digunakan untuk menunjuk state berikutnya. Finite automata edge dapat berisi beberapa method
    """
    def __init__(self, next_node, edge: str = EPSILON, is_data=True):
        self.next_node = next_node
        self.edge: str = edge
        self.is_data = is_data

    def evaluate(self, string_a: str) -> bool:
        if self.edge == string_a:
            return True
        
        return False
    
    def set_finite_automata(self, param):
        self.next_node = param

    def next_finite_automata(self) :
        return self.next_node