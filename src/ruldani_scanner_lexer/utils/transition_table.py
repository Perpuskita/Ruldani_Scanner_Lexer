"""
transisi table adalah sebuah cara mendefinisikan alur dari finite automata
transisi table mem

dalam kelas transisi table diperlukan beberapa variabel diantaranya adalah
Q  : Himpunan state
Σ  : Himpunan input
q0 : Start State
F  : Himpunan accepting state
δ  : Himpunan Fungsi Transisi

"""

from ruldani_scanner_lexer.utils.transition_table_utils import transition_function
from ruldani_scanner_lexer.logging import logging

class table:
    def __init__(self, himpunan_state:list, himpunan_input:list, start_state:str, log: logging=None):
        self.himpunan_state: list = himpunan_state
        self.himpunan_input: list = himpunan_input
        self.start_state: list = start_state
        self.himpunan_accepting_state: list[str] = []

        # membuat list dari fungsi transisi
        self.himpunan_fungsi_transisi:list[transition_function] = []
        for state in himpunan_state :
            himp_transisi: transition_function = transition_function(state=state, input=himpunan_input, jumlah_state=len(himpunan_state))
            self.himpunan_fungsi_transisi.append(himp_transisi)

        if log == None:
            self.log : logging = logging()
        else:
            self.log : logging = log

    def add_transition(self, state:str, input:str, fungsi_transisi:str) -> None:
        state_num: int       = self.num_state(state)
        input_num: int       = self.num_input(input)

        set_himp: transition_function = self.himpunan_fungsi_transisi[state_num]
        set_himp.set_transition(input= input_num, transition_str=fungsi_transisi)

        return -1

    def num_state(self, nama_state: str)-> int :
        for i, nama in enumerate(self.himpunan_state):
            if nama == nama_state :
                return i
        
        print ("state tidak ditemukan")
        return -1

    def num_input(self, nama_input: str)-> int :
        for i, nama in enumerate(self.himpunan_input):
            if nama == nama_input :
                return i
        
        print ("state tidak ditemukan")
        return -1

    def add_accepting_node(self, node: str):
        self.himpunan_accepting_state.append(node)
        return

    def eval(self):
        return

    def show(self):
        self.log.print_table_transition( himpunan_state = self.himpunan_state,
                                         himpunan_input = self.himpunan_input,
                                         himpunan_fungsi_transisi= self.himpunan_fungsi_transisi,
                                         himpunan_accepting_state=self.himpunan_accepting_state,
                                         start_state=self.start_state)