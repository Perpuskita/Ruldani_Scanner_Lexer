import pytest
from ruldani_scanner_lexer.utils.thompson_construction_utils import alternation_thompson, concatination_thompson, klenee_closure_thompson


class ThompsonTest:
    # setup new test
    def setup_class(cls):
        regex: str = ("def|fun")

    # test fitur klenee closure
    def test_klenee_closure(self):
        assert klenee_closure_thompson().make_finite_automata("a") == [] 
    
    def test_concatination(self):
        assert self.re.conc