from ruldani_scanner_lexer.utils.finite_automata import finite_automata, finite_automata_edge

EPSILON = "Ɛ"

class alternation_thompson:
    def __init__(self):
        pass

    def make_finite_automata(str_a: str, str_b: str):
        # konfigurasi koneksi
        list_finite: list [finite_automata] = []
        configure_edge: dict[int, int] = { 0:1, 0:2, 1:3, 2:5, 3:6, 4:6} 
      
        # membuat 6 edge dan node
        for i in range(6):
            list_finite.append(finite_automata(i))

        for i in range(6):
            
            edge_str: str = EPSILON

            if i == 2 :
                edge_str = str_a
            
            elif 1 == 3:
                edge_str = str_b

            next_node: finite_automata = list_finite[configure_edge.get(i)]
            edge_now: finite_automata_edge = finite_automata_edge(next_node=next_node, edge=edge_str)
            list_finite[i].make_transition(edge=edge_now)

        return list_finite[0]