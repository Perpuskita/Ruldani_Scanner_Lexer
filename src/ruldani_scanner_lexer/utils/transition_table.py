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

import shutil
import math
#from .finite_automata_node import finite_automata_node, accepting_node, finite_automata_arrow

# konstanta 
WIDTH_TERMINAL = shutil.get_terminal_size()[0]
BOLD = "\033[3m"
RESET = "\033[0m"

class table:
    def __init__(self, himpunan_state:list, himpunan_input:list, start_state:str):
        self.himpunan_state: list = himpunan_state
        self.himpunan_input: list = himpunan_input
        self.start_state: list = start_state
        self.himpunan_accepting_state = []
        # membuat list dari fungsi transisi

        self.himpunan_fungsi_transisi:list = []
        for state in himpunan_state :
            self.himpunan_fungsi_transisi.append(transition_function(state=state, input=himpunan_input))
        # mendefinisikan class terminal
        self.terminal = terminal_table_transition()

    def add_transition(self, state:str, input:str, fungsi_transisi:list):
        
        return 

    def add_accepting_node(self):
        return

    def eval(self):
        return

    def show(self):
        show_terminal: str = self.terminal.desc ( himpunan_state = self.himpunan_state, 
                                                  himpunan_input = self.himpunan_input, 
                                                  himpunan_fungsi_transisi = self.himpunan_fungsi_transisi,
                                                  himpunan_accepting_state = self.himpunan_accepting_state,
                                                  start_state= self.start_state)
        print(show_terminal)

class transition_function:
    def __init__(self, state: str, input: str):
        self.state = state
        self.input = input
        self.transition = []
    
    def get_state(self)-> str:
        return self.state

    def get_input(self)-> str:
        return self.input

    def set_transition(self, transition_str)-> bool:
        return True

# kelas yang digunakan untuk mengelola printing tabel dari transition tabel
class terminal_table_transition:
    def __init__(self):
        pass

    def sparator(self, message :str):
        slash: str = "=" * math.floor((WIDTH_TERMINAL - len(message))/2)
        header_str: str = f"\n{BOLD}{slash}{message}{slash}{RESET}"
        return header_str + "\n"

    def splash_input(self, input_width: int, input: str = None):
        hasil: str = ""

        if input is None :
            hasil += "-" * ( input_width )
            hasil += "+" 

        else:
            hasil += " " * math.floor((input_width - len(input)) / 2) + input
            hasil += " " * (input_width- len(hasil)) + "|"
            
        return hasil

    def state_and_himpunan_transisi(self, 
                                    fungsi_transisi: list, 
                                    state: str, 
                                    input: list, 
                                    input_width: int):

        hasil: str = ""
        return hasil

    def parse_list(self, list_str: list, nama_list: str):
        hasil = nama_list + " : "
        for temp in list_str: 
            hasil += " " + temp + ","

        return hasil + "\n"

    def desc( self, 
              himpunan_state: list, 
              himpunan_input: list,
              himpunan_fungsi_transisi: list,
              himpunan_accepting_state: list,
              start_state: str )-> str :
        
        input_width: int  = 13
        state_width: int  = 3
        transition_height: int = 3

        splash = f"\n{self.splash_input(state_width)}{self.splash_input(input_width=input_width)*len(himpunan_input)}\n"
        state = "himpunan state"

        fungsi_transisi_str: str = splash
        fungsi_transisi_str += f"   |"

        # sumbu x himpunan input
        for input in himpunan_input :
            fungsi_transisi_str += self.splash_input(input=input, input_width=input_width)

        fungsi_transisi_str += splash

       # sumbu y himpunan state 
        for state in himpunan_state:
            fungsi_transisi_str += state + " |"
            # fungsi_transisi_str += f"{ " " * state_width }|"
            fungsi_transisi_str += splash

        # deskripsi formal
        deskripsi = "\n"
        deskripsi += self.parse_list( himpunan_accepting_state, 
                                     "F ( accepting state )")
        deskripsi += self.parse_list( himpunan_input, 
                                     "Σ ( himpunan input ) ")
        deskripsi += self.parse_list( himpunan_state, 
                                     "Q ( himpunan state ) ")
        deskripsi += self.parse_list([start_state] , 
                                     "s ( start state )    ")
        
        # menampung hasil dari 
        header: str = self.sparator(" show transition table ")
        desc_s: str = self.sparator(" description variable ")
        footer: str = self.sparator(" end transition table ")
        hasil : str = header + fungsi_transisi_str + desc_s + deskripsi + footer
        return hasil

if __name__ == "__main__":
    state = ["q0", "q1", "q2", "q3"]
    input = ["a", "b", "c", "d"]
    start = "q0"



    table_transisi = table(state, input, start)
    table_transisi.show()