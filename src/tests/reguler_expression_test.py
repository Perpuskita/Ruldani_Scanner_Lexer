
import os
import sys

# system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ruldani_scanner_lexer.reguler_expression import reguler_expression


def reguler_expression_concatination ():
    return None

def reguler_expression_klenee_closure():
    return None

def reguler_expression_alternation():
    return None



# testing untuk class reguler expression
if __name__ == "__main__":
    print("yes")
    
    # testing regex
    re = reguler_expression("(ab)*|(dc)*")
    re.leaguage_of_s(7)

    # # testing concatination (ab)
    # re.concatination("n","s")
    # re.concatination(None, "t")
    # re.concatination("t", None )
    
    # # testing klenee_closure (a*)
    # re.klenee_closure("r")
    # re.klenee_closure("r", 5)
    # re.klenee_closure(None)

    # # testing alternation (a|b)
    # re.alternation("n", "s")
    # re.alternation(None, "s")
    # re.alternation("n", None)
