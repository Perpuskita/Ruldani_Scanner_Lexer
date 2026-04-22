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
        self.read_expression(self.expression_ast)

    # fungsi untuk membaca AST atau expression
    def read_expression(self, expression_ast: expression):
        lhs = expression_ast.lhs
        rhs = expression_ast.rhs
        op  = expression_ast.operator
        
        if type(lhs) == expression and type(rhs) == expression :
            self.read_expression(lhs)
            self.read_expression(rhs)
            self.make_thompson_construction(lhs=EPSILON, op=op.get_token(), rhs=EPSILON)

        elif type(lhs) ==  expression and type(rhs) != expression :
            self.make_thompson_construction(lhs=EPSILON, op=op.get_token(), rhs=rhs.get_token())
            self.read_expression(lhs)

        elif type(lhs) != expression and type(rhs) == expression :
            self.make_thompson_construction(lhs=EPSILON, op=op.get_token(), rhs=rhs.get_token())
            self.read_expression(rhs)

        else:
            self.make_thompson_construction(lhs=lhs.get_token(), op=op.get_token(), rhs=rhs.get_token())
        
        return None
    
    def make_combine(self, op: str, lhs: str, rhs:str ):
        
        return None

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
        return None
    
    # fungsi mengubah concatination ke NFA
    def make_concatination(self, stra: str = EPSILON, strb: str = EPSILON) -> list[finite_automata]:
        self.concatination.make_finite_automata( str_a = stra, str_b = strb)
        return None
    
    # fungsi mengubah klenee closure ke NFA
    def make_klenee_closure(self, stra: str = EPSILON) -> list[finite_automata]:
        self.klenee_closure.make_finite_automata(str_a=stra)
        return None
    
    # fungsi untuk menggabungkan hasil dari make 
    def combine(self, base: finite_automata_edge, head: finite_automata, tail: finite_automata ):
        
        temp: finite_automata = base.next_node
        base.next_node = head
        tail.next_node = temp

        return None
    
    # fungsi untuk menggeser nilai dari squence
    
    # fungsi 