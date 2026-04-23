from ruldani_scanner_lexer.utils.thompson_construction_utils.thompson_construction_abstract import thompson_constraction_abstract
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge
from ruldani_scanner_lexer.constant import EPSILON

class alternation_thompson(thompson_constraction_abstract):
    def __init__(self):
        self.configure_edge: tuple[int, int] = ((0,1), (0,2), (1,3), (2,4), (3,5), (4,5)) 
        pass

    def make_finite_automata(self, str_a: str, str_b: str) -> list[finite_automata]:
        # konfigurasi koneksi
        list_finite: list [finite_automata] = []
      
        # membuat 6 edge dan node
        for i in range(6):
            list_finite.append(finite_automata(i))

        for i in range(6):
            
            edge_str: str = EPSILON

            if i == 2 :
                edge_str = str_a
            
            elif i == 3:
                edge_str = str_b

            node_a: int = self.configure_edge[i][0]
            node_b: int = self.configure_edge[i][1]

            next_node: finite_automata = list_finite[node_b]
            edge_now: finite_automata_edge = finite_automata_edge(next_node=next_node, edge=edge_str)
            list_finite[node_a].make_transition(edge=edge_now)
        
        return list_finite
    