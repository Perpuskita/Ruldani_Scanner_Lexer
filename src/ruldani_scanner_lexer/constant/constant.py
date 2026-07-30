# Constant operator REGEX
EPSILON: str = "ε"
ALTERNATION: str = "|"
KLENEE_CLOSURE: str = "*"
CONCATINATION: str = "+"

# Configuration NFA
ALTERNATION_NFA: tuple[int, int] = ((0,1), (0,2), (1,3), (2,4), (3,5), (4,5))
KLENEE_CLOSURE_NFA: tuple[int, int] = ((0,1), (0,3), (1,2), (2,3), (3,0))
CONCATINATION_NFA: tuple[int, int] = ((0,1), (1,2), (2,3))