from ruldani_scanner_lexer.utils.thompson_construction_utils.thompson_construction_abstract import thompson_constraction_abstract
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge
from ruldani_scanner_lexer.constant import EPSILON


class concatination_thompson(thompson_constraction_abstract):
    def __init__(self):
        self.configure_edge: tuple[int,int] = ((0,1), (1,2), (2,3)) 
        pass

    def make_finite_automata(self, str_a: str, str_b: str) -> list[finite_automata]:
        # konfigurasi koneksi
        list_finite: list [finite_automata] = []
      
        # membuat 4 node
        for i in range(4):
            list_finite.append(finite_automata(i))

        # membuat 3 edge
        for i in range(3):
            
            edge_str: str = EPSILON

            if i == 0 :
                edge_str = str_a
            
            elif i == 2:
                edge_str = str_b

            node_a: int = self.configure_edge[i][0]
            node_b: int = self.configure_edge[i][1]

            next_node: finite_automata = list_finite[node_b]
            edge_now: finite_automata_edge = finite_automata_edge(next_node=next_node, edge=edge_str)
            list_finite[node_a].make_transition(edge=edge_now)

        return list_finite
    
