from ruldani_scanner_lexer.utils.transition_table import table

if __name__ == "__main__":
    
    # deklarasi state, input dan start dari node i 
    state = ["q0", "q1", "q2", "q3", "q4"]
    input = ["a", "b", "c", "d", "epsilon"]
    start = "q0"

    table_transisi = table(state, input, start)

    # menambahkan fungsi transisi

    table_transisi.add_transition(state="q0", input="a", fungsi_transisi="q1")
    table_transisi.add_transition(state="q0", input="c", fungsi_transisi="q1")
    table_transisi.add_transition(state="q1", input="b", fungsi_transisi="q2")
    table_transisi.add_transition(state="q2", input="c", fungsi_transisi="q2")
    table_transisi.add_transition(state="q2", input="c", fungsi_transisi="q3")
    table_transisi.add_transition(state="q2", input="c", fungsi_transisi="q1")
    table_transisi.add_transition(state="q2", input="c", fungsi_transisi="q0")

    # menambahkan accepting node
    table_transisi.add_accepting_node(node="q2")

    # menampilkan tabel transisi
    table_transisi.show()