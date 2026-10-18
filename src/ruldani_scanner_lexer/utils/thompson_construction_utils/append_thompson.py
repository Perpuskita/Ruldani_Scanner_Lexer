from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge
from ruldani_scanner_lexer.utils.thompson_construction_utils.alternation_thompson import alternation_thompson
from ruldani_scanner_lexer.utils.thompson_construction_utils.concatination_thompson import concatination_thompson
from ruldani_scanner_lexer.utils.thompson_construction_utils.klenee_closure_thompson import klenee_closure_thompson
from ruldani_scanner_lexer.constant import EPSILON


class append_thompson():
    def __init__(self):
        pass

    def append_on_alternation(  self, param_a: list[finite_automata] = None,
                                param_b: list[finite_automata] = None ) -> list[finite_automata]:
        
        root: list[finite_automata] = alternation_thompson().make_finite_automata(EPSILON, EPSILON)

        # mengembalikan nilai jika kedua parameter adalah NONE
        if len(param_a) == None and len(param_b) == None:
            print("input salah")
            return None
        
        # mengambil finite automata dari root 
        root_a: finite_automata_edge = root[0].next[0]
        root_b: finite_automata_edge = root[0].next[1]
        tail_a: finite_automata_edge = root[3].next[0]
        tail_b: finite_automata_edge = root[4].next[0]
        
        # menyambungkan tail dan head parameter
        # kondisi jika param a diberikan
        if len(param_a) > 0:
            # set next finite automata ke param a[0]
            root_a.set_finite_automata(param_a[0])

            # set param a terakhir menjadi tail
            param_a[-1].next_node(tail_a)

        # kondisi jika param a diberikan
        if len(param_b) > 0:
            # set next finite automata ke param a[0]
            root_b.set_finite_automata(param_b[0])

            # set param a terakhir menjadi tail
            param_b[-1].next_node(tail_b)
        
        del(root[2:4])
        return self.rename_node_info(queue_node=[root[0]])

    def append_on_concatination( self,
                                 param_a: list[finite_automata] = None,
                                 param_b: list[finite_automata] = None ) -> list[finite_automata]:
        

        # mengembalikan nilai jika kedua parameter adalah NONE
        if param_a == None and param_b == None:
            print("input salah")
            return None
        
        epsilon_transition: finite_automata_edge = finite_automata_edge(next_node=param_b[0])
        param_a[-1].next = [epsilon_transition]

        result =  param_a + param_b
        return self.rename_node_info([result[0]])

    def append_on_klenee_closure(self, param_a: list[finite_automata]):
        root: list[finite_automata] = klenee_closure_thompson().make_finite_automata(EPSILON)

        head: finite_automata_edge = root[0].next[0]
        tail: finite_automata_edge = root[2].next[0]

        head.next_node = param_a[0]
        param_a[-1].next = [tail]

        del(root[1:2])
        return self.rename_node_info([root[0]])

    def rename_node_info(self, queue_node: list[finite_automata]):
        
        new_root: list[finite_automata] = []
        is_counter: dict[finite_automata] = {}
        name_factor: int = 0
        
        # while loop untuk mendapatkan node
        while len(queue_node) > 0 :
            node: finite_automata = queue_node.pop(0)
            if node in is_counter:
                continue

            # assign node menjadi key dalam is counter
            is_counter[node] = True

            # mengubah nama node menjadi name val
            node.name = name_factor
            name_factor += 1
            
            # jika node >= 1
            if len(node.next) > 0 :
                for edge in node.next :
                    if edge.is_data :
                        queue_node.append(edge.next_node)
            
            new_root.append(node)
        return new_root