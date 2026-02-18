'''
nondeterministic finite automata adalah sebuah kelas yang bertanggung jawab untuk
menampung finite automata state. operasi yang bisa dilakukan disini adalah 
menambahkan node, set start state, set accepting node, compile dan draw.
'''

from ruldani_scanner_lexer.utils import table, finite_automata_node, accepting_node, finite_automata_edge
from ruldani_scanner_lexer.exceptions import nondeterministic_finite_automata_error, nondeterministic_finite_automata_warning

class nondeterministic_finite_automata:
    def __init__(self):

        self.accepting_node : list [accepting_node] = []
        self.fungsi_transisi : list [finite_automata_edge] = []
        self.state : list [finite_automata_node] = []
        self.start_state :list [finite_automata_edge] = []
        self.compiled = False

    def add_node(self, state:str) -> finite_automata_node:
        self.compiled = False
        # cek apakah sudah terdefinisikan
        # y warning, n tambahkan
        for states in self.state :
            nama_state: str = states.get_node()
            if nama_state == state:
                print("warning double entry")
                return state

        # inisialisai dari node baru dengan nama state
        new_node: finite_automata_node = finite_automata_node(state)
        self.state.append(new_node)
        
        # return node baru yang telah digenerate
        return new_node

    def set_start_state(self, state: finite_automata_node):
        self.compiled = False

        # cek apakah state yang dimaksud ada ?
        # jika tidak error 400
        cek_state: bool = False
        for states in self.state :
            if state == states:
                cek_state = True

        if not cek_state :
            print("warning state tidak ada")
            return None
        
        # apakah sudah dimasukan ?
        # y. tambahkan state kedalam start state
        # n. jika sudah dimasukan warning double entry

        for states in self.start_state :
            if states == state:
                print(f"warning double entry on start state {state.get_node()}")
                return states
        
        new_start_state = self.start_state.append(state)
        return new_start_state

    def set_accepting_node(self, state: finite_automata_node):
        self.compiled = False

        # cek apakah dudah terdefinisikan 
        # cek apakah state yang dimaksud ada ?
        # jika tidak error 400
        cek_state: bool = False
        for states in self.state :
            if state == states:
                cek_state = True

        if not cek_state :
            print("warning state tidak ada")
            return None
        
        # apakah sudah dimasukan ?
        # y. tambahkan state kedalam start state
        # n. jika sudah dimasukan warning double entry

        for states in self.accepting_node :
            if states.get_node() == state:
                print(f"warning double entry in accepting node {state.get_node()}")
                return states

        # tambahkan ke dalam
        new_accepting_node = accepting_node(state)
        self.accepting_node.append(new_accepting_node)
        return new_accepting_node
 
    def compile(self):
        if self.compiled :
            print("compile")
        else :
            cek: bool = True
            # cek apakah start state sudah terisi
            if len(self.start_state) == 0 :
                cek = False
                print ("start state tidak terdeterksi")
            
            if len(self.fungsi_transisi) == 0 :
                cek = False
                print ("fungsi transisi tidak terdeteksi")
                
            if len(self.state) == 0 :
                print("state tidak terdeteksi")
                cek = False

            if len(self.accepting_node) == 0 :
                print("accepting node tidak terdeteksi")
                cek = False

            if not cek :
                return False
             
            # cek apakah accepting node dan node saling terhubung
            # cek apakah ada accepting state
            # y. lanjut self.compiled = true
            # n. error return 500
            print("cek dulu")
            self.compiled = True

        return True # ganti none nanti

    def set_finite_automata_edge(self):
        return None

    def eval(self):
        return None

    def generate_image(self):
        return None


if __name__ == "__main__" :
    nfa : nondeterministic_finite_automata = nondeterministic_finite_automata()
    q0  : finite_automata_node = nfa.add_node("q0")
    q1  : finite_automata_node = nfa.add_node("q1")

    nfa.set_start_state(q1)
    nfa.set_accepting_node(q1)

    nfa.compile()


    