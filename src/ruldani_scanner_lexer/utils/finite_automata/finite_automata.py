from ruldani_scanner_lexer.utils.finite_automata.finite_automata_edge import finite_automata_edge

class finite_automata:
    """
    finite automata node merupakan sebuah node yang berisi state 
    pada finite automata. Finite automata dilambangkan dengan lingkaran.
    node atau state ini memiliki sejumlah transisi yang dilambangkan dengan panah.
    """
    def __init__(self, name: int):
        
        self.expression = None
        self.next: list[finite_automata_edge] = []
        self.accepting: bool = False
        self.start_state: bool = False
        self.name: int = name
    
    def make_transition(self, edge: finite_automata_edge):
        self.next.append(edge)
        return None
    
    def set_accepting(self) -> None:
        self.accepting = True
        return None
    
    def is_accepting(self) -> None:
        return self.accepting
    
    def set_start_state(self) -> None:
        self.start_state = True
        return None
    
    def is_start_state(self) -> None:
        return self.start_state

    def eval_finite_automata_edge(self, char: str):
        for finite_edge in self.next :
            if(finite_edge.evaluate(char)):
                return finite_edge.next_finite_automata()
        return None

    def next_node(self, node_s):
        self.next.append(node_s)
        return None
