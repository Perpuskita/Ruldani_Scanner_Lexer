from ruldani_scanner_lexer.utils.finite_automata.finite_automata import finite_automata

class finite_automata_edge:
    """
    finite auromata arrow edge digunakan untuk menunjuk state berikutnya. Finite automata edge dapat berisi beberapa method
    """
    def __init__(self, edge: str, next_node: finite_automata):
        self.next_node: finite_automata = next_node
        self.edge: str = edge

    def evaluate(self, string_a: str) -> bool:
        if self.edge == string_a:
            return True
        
        return False
    
    def next_finite_automata(self) -> finite_automata :
        return self.next_node