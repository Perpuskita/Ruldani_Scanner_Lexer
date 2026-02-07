
import os
import sys
import pytest

# add src path to directory system
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ruldani_scanner_lexer.reguler_expression import reguler_expression


# test sub feature
class TestSubFeature:
    """
    Tes sub feature adalah unitest untuk testing sub fitur dalam class.
    
    fitur yang di tes diantaranya adalah: 
    klenee closure, 
    concatination dan 
    alternation
    
    testing fitur ini memastikan fitur utama dalam kelas reguler expression
    dapat berjalan dengan baik dan sesuai alur program.
    """

    # setup new test
    def setup_class(cls):
        cls.re = reguler_expression("")

    # test fitur klenee closure
    def test_klenee_closure(self):
        assert self.re.klenee_closure("r") == ["r", "rr"]
    
    def test_klenee_closure2(self):
        assert self.re.klenee_closure("r",2) == ["r", "rr"]

    def test_klenee_closure3(self):
        assert self.re.klenee_closure("r",3) == ["r", "rr", "rrr"]

    # test fitur concatination
    def test_concatination(self):
        assert self.re.concatination("a","b") == ["ab"]

    def test_concatination2(self):
        assert self.re.concatination("a", None) == None

# tes fitur utama
class TestCoreFeature:
    """
    Fitur yang di tes dalam fitur utama adalah compile dan juga eval

    compile menghasilkan kemungkinan hasil dari reguler expression yang dihasilkan
    eval mengevaluasi input string terhadap reguler expression yang telah dicompile
    """
    # setup new class 
    def setup_class(cls):
        cls.list_test = ["ab", "a|b", 
                         "a*"
                         "ab|c", 
                         "(ab)|c",
                         "ab|c*", 
                         "a(b|c)*"
                         "(ab|c)*"] 
        cls.re = reguler_expression("a+b")

    def test_regex_1(self):
        assert True

    def test_regex_2(self):
        assert True
    
    def test_regex_3(self):
        assert True
    
    def test_regex_4(self):
        assert True
    
    def test_regex_5(self):
        assert True
