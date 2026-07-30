from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge
from ruldani_scanner_lexer.constant import EPSILON

class append_thompson():
    def __init__(self):
        self.alternation_head: tuple = (3,4)
        self.concatination_head: tuple = (2,3)
        self.klenee_closure_head: tuple = (3)

    def append_on_alternation(  self, root: list[finite_automata] = None, 
                                param_a: list[finite_automata] = None,
                                param_b: list[finite_automata] = None ) -> list[finite_automata]:
        
        if root == None :
            print("root salah")
            return None

        # mengembalikan nilai jika kedua parameter adalah NONE
        if len(param_a) == None and len(param_b) == None:
            print("input salah")
            return None
        
        # mengambil finite automata dari root 
        root_a: finite_automata_edge = root[0].next[0]
        root_b: finite_automata_edge = root[0].next[1]
        tail_a: finite_automata_edge = root[3].next[0]
        tail_b: finite_automata_edge = root[4].next[0]

        #shifting mechanic root
        new_root : list[finite_automata] = []
        tail: list[finite_automata] = root[-1]

        tail.name += len(param_a) + len(param_b) - 4
        new_root.append(root[0])

        queue: list[finite_automata] = [param_a[0], param_b[0]]
        name_val: int = 1

        is_counter: dict[finite_automata] = {}
        
        # while loop untuk mendapatkan node
        while len(queue) > 0 :
            node: finite_automata = queue.pop(0)
            if node in is_counter:
                continue

            # assign node menjadi key dalam is counter
            is_counter[node] = True

            # mengubah nama node menjadi name val
            node.name = name_val
            name_val += 1
            
            for edge in node.next :
                queue.append(edge.next_node)

            new_root.append(node)
            
        # menyambungkan tail dan head
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
        
        del root[1:4]
        return new_root

    def append_on_concatination( self, root: list[finite_automata] = None, 
                                 param_a: list[finite_automata] = None,
                                 param_b: list[finite_automata] = None ) -> list[finite_automata]:
        
        
        if root == None :
            print("root salah")
            return None

        # mengembalikan nilai jika kedua parameter adalah NONE
        if len(param_a) == None and len(param_b) == None:
            print("input salah")
            return None
        
        # save head a and b
        head_a: finite_automata_edge = root[0].next_node[0]
        head_b: finite_automata_edge = root[2].next_node[0]

        # menyambungkan head dan tail
        # kondisi jika param a sesuai

        
        # kondisi jika param b sesuai

        return None