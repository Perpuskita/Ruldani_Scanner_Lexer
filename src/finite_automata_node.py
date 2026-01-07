class finite_automata_node:
    def __init__(self):
        print("inisialisasi node berhasil")
        self.expression = None
        self.next_state = []
        self.accepting_states = False
    
    def print_node(self):
        return None

    def set_expression(self, expression: str):
        self.expression = expression
        return None

    def set_accepting_states(self):
        self.accepting_states = True

