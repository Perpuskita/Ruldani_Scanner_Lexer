from pluggy import HookImpl
from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson, klenee_closure_thompson, concatination_thompson, append_thompson, print_thompson
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, token
from ruldani_scanner_lexer.constant import EPSILON, CONCATINATION, ALTERNATION, KLENEE_CLOSURE

class thompson_construction:
    def __init__(self, expression_ast: expression):

        # class untuk membuat tools thompson construction
        self.concatination: concatination_thompson = concatination_thompson()
        self.alternation: alternation_thompson = alternation_thompson()
        self.klenee_closure: klenee_closure_thompson = klenee_closure_thompson()

        self.append_thompson: append_thompson = append_thompson()

        # menampung hasil dari finite automata yang telah digenerate
        self.finite_automata: list[finite_automata] = []

        # inisialisasi ast atau expression
        self.expression_ast: expression = expression_ast
        self.fa: list[finite_automata] = self.make_nfa(expression_ast=self.expression_ast)
        
        # mengambil informasi state, input dan transisi di fa
        self.himpunan_state: list[str] = [f"q{i}" for i in range(0, len(self.fa)-1)]
        self.himpunan_input: list[str] = []
        self.transisi: list[str, str, str] = []
        
        # membuat dan memuat himpunan transisi
        self.get_himpunan_transisi()

    # fungsi untuk membaca AST dan mengubahnya menjadi finite automata
    def make_nfa(self, expression_ast: expression) -> list[finite_automata]:
        lhs: token = expression_ast.lhs
        rhs: token = expression_ast.rhs
        op: token  = expression_ast.operator
        
        lhs_res: list[finite_automata] = []
        rhs_res: list[finite_automata] = []

        if type(lhs) == expression :
            lhs_res = self.make_nfa(lhs)
        else:
            lhs_res = self.make_atom(str_a=lhs.get_token())

        if type(rhs) == expression :
            rhs_res = self.make_nfa(rhs)
        else:
            rhs_res = self.make_atom(str_a=rhs.get_token())
        
        # return
        return self.append_thompson_construction(op = op.get_token(), lhs=lhs_res, rhs=rhs_res)

    # membuat sebuah finite automata dengan tail str_a
    def make_atom(self, str_a:str) -> list[finite_automata]:
        head: finite_automata = finite_automata(0)
        tail: finite_automata = finite_automata(0)
        edge: finite_automata_edge = finite_automata_edge(next_node=tail, edge=str_a)
        head.make_transition(edge)
        return [head,tail]

    # menggabungkan antara dua thomson dengan construction 
    def append_thompson_construction(self, op: str, lhs: list[finite_automata], rhs: list[finite_automata]) -> list[finite_automata]:
        if op == CONCATINATION :
            return self.append_thompson.append_on_concatination(param_a=lhs,param_b=rhs)
        
        elif op == ALTERNATION :
            return self.append_thompson.append_on_alternation(param_a=lhs,param_b=rhs)

        elif op == KLENEE_CLOSURE:
            return self.append_thompson.append_on_klenee_closure(param_a=lhs)
                    
        return None

    # membuat thompson construction berdasarkan lhs dan rhs
    def make_thompson_construction(self, lhs: str, op: str, rhs: str) -> list[finite_automata]:

        if op == CONCATINATION:
            return self.make_concatination(lhs, rhs)
        
        elif op == ALTERNATION :
            return self.make_alternation(lhs, rhs)

        elif op == KLENEE_CLOSURE:
            return self.make_alternation(rhs)
        
        else :
            raise ValueError("operator token not valid")

    # fungsi mengubah alternation ke NFA
    def make_alternation(self, stra: str = EPSILON, strb: str = EPSILON) -> list[finite_automata]:
        result = self.alternation.make_finite_automata( str_a = stra, str_b = strb)
        return result
    
    # fungsi mengubah concatination ke NFA
    def make_concatination(self, stra: str = EPSILON, strb: str = EPSILON) -> list[finite_automata]:
        result = self.concatination.make_finite_automata( str_a = stra, str_b = strb)
        return result
    
    # fungsi mengubah klenee closure ke NFA
    def make_klenee_closure(self, stra: str = EPSILON) -> list[finite_automata]:
        result = self.klenee_closure.make_finite_automata(str_a=stra)
        return result
    
    # fungsi untuk menggabungkan hasil dari make 
    def combine(self, base: finite_automata_edge, head: finite_automata, tail: finite_automata ):
        empty_edge: finite_automata_edge = finite_automata_edge(base.next_node, edge=EPSILON)
        base.next_node = head
        tail.next_node(empty_edge)
        return None
    
    # fungsi untuk mencetak hasil dari pembuatan ast
    def print_list_nfa(self) -> str:
        return self.concatination.print_finite_automata(self.fa)

    # memuat himpunan transisi yang didapatkan dari self finite automata
    # hasilnya berupa list
    def get_himpunan_transisi(self) -> None:

        # make chamber for himpunan input dan himpunan state
        set_input: set[str] = set()

        # make chamber for loop
        hasil: list[str,str,str] = []
        queue: list[finite_automata] = [self.fa[0]]

        # membuat loop untuk menangani
        while len(queue) >= 1:
            now: finite_automata = queue.pop()

            for node in now.next:
                state: str = f"q{now.name}"
                inputs: str = node.edge
                transisi: str = f"q{node.next_node.name}"

                info: list[str, str, str] = [state, inputs, transisi ]
                hasil.append(info)
                queue.append(node.next_node)
                set_input.add(inputs)

        self.himpunan_input = list(set_input)
        self.transisi = hasil

        return None