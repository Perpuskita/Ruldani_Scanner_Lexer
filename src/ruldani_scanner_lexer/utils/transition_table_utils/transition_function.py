"""
transition function adalah kelas yang menangani perilaku dari himpunan fungsi transisi 
δ  : Himpunan Fungsi Transisi

"""
from ruldani_scanner_lexer.utils.transition_table_utils.transition_boolean import transition_boolean

class transition_function:
    def __init__(self, state: str, input: list, jumlah_state: int):
        self.state = state
        self.input = input

        # menambahkan transisi sejumlah input
        self.transition: list = []
        for i in range(len(input)):
            transition_b = transition_boolean()
            self.transition.append(transition_b)

    def set_transition(self, transition_str: str, input: int )-> int:
        self.transition[input].add_transition(transition_str)
        return True

    def get_transition(self):
        hasil: list = []
        for i, trans in enumerate(self.transition):
            hasil.append(trans.get_transition())
        return hasil