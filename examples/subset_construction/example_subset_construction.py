from ruldani_scanner_lexer.constant import EPSILON
from ruldani_scanner_lexer.utils.transition_table import table
from ruldani_scanner_lexer.utils.subset_construction import subset_construction

if __name__ == "__main__":
    
    # deklarasi state, input dan start dari node i 
    state   = ["q0", "q1", "q2"]
    input_s = ["a", "b" ]
    start   = "q0"

    table_transisi = table(state, input_s, start)

    # menambahkan fungsi transisi

    table_transisi.add_transition(state="q0", input="a", fungsi_transisi="q0")
    table_transisi.add_transition(state="q0", input="a", fungsi_transisi="q1")
    table_transisi.add_transition(state="q0", input="b", fungsi_transisi="q2")
    table_transisi.add_transition(state="q1", input="a", fungsi_transisi="q0")
    table_transisi.add_transition(state="q1", input="b", fungsi_transisi="q1")
    table_transisi.add_transition(state="q2", input="b", fungsi_transisi="q0")
    table_transisi.add_transition(state="q2", input="b", fungsi_transisi="q1")

    # menambahkan accepting node
    table_transisi.add_accepting_node(node="q2")

    # subset_construction
    subset_cons: subset_construction = subset_construction(nfa_table=table_transisi)

