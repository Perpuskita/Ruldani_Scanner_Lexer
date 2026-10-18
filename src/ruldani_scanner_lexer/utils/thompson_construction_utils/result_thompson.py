from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge

class print_thompson:
    def __init__(self, list_finite: list[finite_automata] ) -> None:
        self.list_finite = list_finite
    
    def compare_thompson(self, list_compare: list) -> bool :
        '''
        Membandingkan hasil dari print thompson
        dengan list yang diberikan, format

        q0 -> q1 = ε
        q0 -> q3 = ε
        q1 -> q2 = a
        q2 -> q3 = ε
        q3 -> q0 = ε

        '''

        hasil = self.print_thompson()
        if hasil == list_compare :
            return True        
        else :
            return False

    def print_thompson(self) -> tuple:
        '''
        Mengubah list finite menjadi tuple
        '''

        result: tuple = ()
        temp_list: list[str] = []

        for nodes in self.list_finite:
            for node in nodes.next :
                temp_list.append(f"q{nodes.name} -> q{node.next_node.name} = {node.edge}")

        result = tuple(temp_list)

        return result
    
    def reverse_list_thompson(self) -> list[finite_automata] :
        '''
        Membalik proses print menjadi list finite automata
        '''

        # not implement yet
        return None
     
    def animate(self) -> None:
        '''
        Membuat animasi atau tampilan dari list finite
        '''

        # not implement yet
        return None