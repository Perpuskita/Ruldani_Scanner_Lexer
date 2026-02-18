import pytest
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
    def setup_class(cls):
        cls.re = reguler_expression("ab")

    # setup new class 
    def test_regex_1(self):
        assert self.re.compile() == ['ab']

    def test_regex_2(self):
        assert True
    
    def test_regex_3(self):
        assert True
    
    def test_regex_4(self):
        assert True
    
    def test_regex_5(self):
        assert True
