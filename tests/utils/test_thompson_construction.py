import pytest
from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson, concatination_thompson, klenee_closure_thompson
from ruldani_scanner_lexer.utils.finite_automata_utils import finite_automata
from ruldani_scanner_lexer.utils.thompson_construction_utils import append_thompson

class TestThompson:
    # setup new test
    def setup_class(cls):
        regex: str = ("def|fun")
        
    #setup new test data
    @pytest.fixture(autouse=True)
    def setup_test_data(self):
        concatination_thompson_converter: concatination_thompson = concatination_thompson()
        alternation_thompson_converter: alternation_thompson = alternation_thompson()
        klenee_closure_thompson_converter: klenee_closure_thompson = klenee_closure_thompson()

        self.param_a: list[finite_automata] = concatination_thompson_converter.make_finite_automata("a","b")
        self.param_b: list[finite_automata] = concatination_thompson_converter.make_finite_automata("b","c")
        
        self.param_c: list[finite_automata] = alternation_thompson_converter.make_finite_automata("a", "b")
        self.param_d: list[finite_automata] = alternation_thompson_converter.make_finite_automata("b","c")
        
        self.param_e: list[finite_automata] = klenee_closure_thompson_converter.make_finite_automata("a")
        self.param_f: list[finite_automata] = klenee_closure_thompson_converter.make_finite_automata("b")

        self.converter = concatination_thompson_converter
        self.append: append_thompson = append_thompson()

    def test_concationation(self):
        assert self.converter.print_finite_automata(self.param_a) == f"q0 -> q1 = a\nq1 -> q2 = ε\nq2 -> q3 = b\n"

    def test_alternation(self):
        assert self.converter.print_finite_automata(self.param_c) == f"q0 -> q1 = ε\nq0 -> q2 = ε\nq1 -> q3 = a\nq2 -> q4 = b\nq3 -> q5 = ε\nq4 -> q5 = ε\n"
    
    def test_klenee_closure(self):
        assert self.converter.print_finite_automata(self.param_e) == f"q0 -> q1 = ε\nq0 -> q3 = ε\nq1 -> q2 = a\nq2 -> q3 = ε\nq3 -> q0 = ε\n"

    def test_append_concationation(self):
        hasil: list[finite_automata] = self.append.append_on_concatination(param_a=self.param_a, param_b=self.param_b)
        res = self.converter.print_finite_automata(hasil)
        assert res == f"q0 -> q1 = a\nq1 -> q2 = ε\nq2 -> q3 = b\nq3 -> q4 = Ɛ\nq4 -> q5 = b\nq5 -> q6 = ε\nq6 -> q7 = c\n"
    
    def test_append_alternation(self):
        hasil: list[finite_automata] = self.append.append_on_alternation(param_a=self.param_a, param_b=self.param_b)
        res = self.converter.print_finite_automata(hasil)
        assert res == f"q0 -> q1 = ε\nq0 -> q2 = ε\nq1 -> q3 = a\nq2 -> q4 = b\nq3 -> q5 = ε\nq4 -> q6 = ε\nq5 -> q7 = b\nq6 -> q8 = c\nq7 -> q9 = ε\nq8 -> q9 = ε\n"

    def test_append_klenee_closure(self):
        hasil: list[finite_automata] = self.append.append_on_klenee_closure(param_a=self.param_a)
        res = self.converter.print_finite_automata(hasil)
        assert res == f"q0 -> q1 = ε\nq0 -> q5 = ε\nq1 -> q2 = a\nq2 -> q3 = ε\nq3 -> q4 = b\nq4 -> q5 = ε\nq5 -> q0 = ε\n"
