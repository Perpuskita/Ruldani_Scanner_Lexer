import pytest
from ruldani_scanner_lexer.utils import pratt_parsing, thompson_construction


class ThompsonTest:
    # setup new test
    def setup_class(cls):
        regex: str = ("def|fun") 
        parser  = pratt_parsing(regex)
        ast     = parser.parse_expression()

    # test fitur klenee closure
    def test_klenee_closure(self):
        assert self.re.klenee_closure("r") == ["r", "rr"]
    