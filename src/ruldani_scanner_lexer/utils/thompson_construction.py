from ruldani_scanner_lexer import nondeterministic_finite_automata
from ruldani_scanner_lexer.utils import pratt_parsing
from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson, klenee_closure_thompson, concatination_thompson
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata, finite_automata_edge
from ruldani_scanner_lexer.utils.pratt_parser_utils import expression, token
from ruldani_scanner_lexer.constant import EPSILON, CONCATINATION, ALTERNATION, KLENEE_CLOSURE

class thompson_construction:
    def __init__(self, expression_ast: expression):

        # class untuk membuat tools thompson construction
        self.concatination: concatination_thompson = concatination_thompson()
        self.alternation: alternation_thompson = alternation_thompson()
        self.klenee_closure: klenee_closure_thompson = klenee_closure_thompson()

        # menampung hasil dari finite automata yang telah digenerate
        self.finite_automata: list[finite_automata] = []

        # inisialisasi ast atau expression
        self.expression_ast: expression = expression_ast

        # nondeterministic finite automata
        self.listing: list[finite_automata] = self.read_expression(self.expression_ast)

    # fungsi untuk membaca AST atau expression
    def read_expression(self, expression_ast: expression) -> list[finite_automata]:
        lhs = expression_ast.lhs
        rhs = expression_ast.rhs
        op  = expression_ast.operator
        
        if type(lhs) == expression and type(rhs) == expression :
            lhss = self.read_expression(lhs)
            rhss = self.read_expression(rhs)
            new  = self.make_thompson_construction(lhs=EPSILON, op=op.get_token(), rhs=EPSILON)
            return self.make_combine(op=op.get_token(), lhs=lhss, rhs=rhss, new_list=new)

        elif type(lhs) ==  expression and type(rhs) != expression :
            new  = self.make_thompson_construction(lhs=EPSILON, op=op.get_token(), rhs=rhs.get_token())
            lhss = self.read_expression(lhs)
            rhss = [rhs.get_token()]
            return self.make_combine(op=op.get_token(), lhs=lhss, rhs=rhss, new_list=new)

        elif type(lhs) != expression and type(rhs) == expression :
            new  = self.make_thompson_construction(lhs=EPSILON, op=op.get_token(), rhs=rhs.get_token())
            lhss = [lhs.get_token()]
            rhss = self.read_expression(rhs)
            return self.make_combine(op=op.get_token(), lhs=lhss, rhs=rhss, new_list=new)

        # basecase
        else:
            hasil = self.make_thompson_construction(lhs=lhs.get_token(), op=op.get_token(), rhs=rhs.get_token())
            return hasil
    
    def make_combine(self, op: str, lhs: list[finite_automata], rhs: list[finite_automata], new_list: list[finite_automata]):

        # # membuat combine berdasarkan op
        if op == CONCATINATION :
            
            foo : finite_automata_edge = new_list[0].next[0]
            goo : finite_automata_edge = new_list[2].next[0]

            self.combine(base= foo, head= lhs[0], tail=lhs[-1])
            self.combine(base= goo, head= rhs[0], tail=rhs[-1])
            return new_list
        
        elif op == ALTERNATION:
            
            foo : finite_automata_edge = new_list[2].next[0]
            goo : finite_automata_edge = new_list[3].next[0]

            self.combine(base= foo, head= lhs[0], tail=lhs[-1])
            self.combine(base= goo, head= rhs[0], tail=rhs[-1])
            return new_list
        
        elif op == KLENEE_CLOSURE :

            foo: finite_automata_edge = new_list[2].next[0]

            if len(lhs) > 1 :
                self.combine(base=foo, head= lhs[0], tail=lhs[-1])
            else :
                self.combine(base=foo, head= rhs[0], tail=lhs[-1])
            
            return new_list

        else:
            raise ValueError("operation tidak valid")

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
    
    def squence_shifting(self):
        return None
    # fungsi untuk menggeser nilai dari squence
    
    # fungsi untuk mencetak hasil dari pembuatan ast
    def print_listing(self, lists: finite_automata):
        
        print(f"q{lists.name}-------------")
        for node in lists.next :
            print(f" - {node.edge}")
            self.print_listing(node.next_node)
        return None