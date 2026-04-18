import shutil
import math

# konstanta 
WIDTH_TERMINAL = shutil.get_terminal_size()[0]
BOLD = "\033[3m"
RESET = "\033[0m"

# kelas yang digunakan untuk mengelola printing tabel dari transition tabel
class terminal_table_transition:
    def __init__(self):
        pass

    def sparator(self, message :str):
        WIDTH_SEPARATOR = 100
        if WIDTH_TERMINAL < 100 :
            WIDTH_SEPARATOR = WIDTH_TERMINAL

        slash: str = "=" * math.floor((WIDTH_SEPARATOR - len(message))/2)
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

    def print_function_transisi_str(self, himp_transisi: list, input_width: int)-> str:
        hasil = ""
        for trans in himp_transisi :
            ln_str: int = len(trans)
            prop: str = " " * math.floor(( input_width - ln_str )/2)
            prop_str:str = f"{prop}{trans}" 
            hasil  += f"{prop_str}{' ' * (input_width - len(prop_str))}|"
        return hasil

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
        for i, state in enumerate( himpunan_state):
            fungsi_transisi_str += state + " |" + self.print_function_transisi_str(himpunan_fungsi_transisi[i], input_width=input_width)
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

