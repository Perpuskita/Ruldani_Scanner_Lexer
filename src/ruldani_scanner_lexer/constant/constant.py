GREETINGS: str ='''
Logger telah diaktifkan
Selamat datang di ruldani scanner lexer

Sebuah project kecil untuk belajar bagaimana sebuah bahasa pemograman digunakan dan dieksekusi
kali ini kita akan mencoba mengubah sebuah code lengkap menjadi token-token yang bisa "dimengerti komputer"
proses inilah yang disebut dengan lexical analysis 

pendekatan yang digunakan adalah dengan menggunakan finite state automata
dimana dalam prosesnya kita akan mengenal beberapa bentuk teori bahasa sebagai berikut

- regex ( reguler expression ) 
- NFA ( Nondeterministic Finite Automata )
- DFA ( Deterministic Finite Automata )
- Minimalized DFA
- Transition table

untuk mengkonversi satu bentuk ke bentuk lainya 
kita akan mengenal teknik teknik dalam teori bahasa
diantaranya adalah

- pratt parsing
- thompson construction
- subset construction
- hopcroft algoritm

untuk melihat bagaimana semua istilah ini bekerja
bisa dibaca di bagian article..

'''


# AST marker
ROOT: str = "└── "
LAST_CHILD: str = "└── "
CHILD: str = "├── "
ROOT_PREFIX: str = "    "
CHILD_PREFIX: str = "│   "


# Constant operator REGEX
EPSILON: str = "ε"
ALTERNATION: str = "|"
KLENEE_CLOSURE: str = "*"
CONCATINATION: str = "+"

# Configuration NFA
ALTERNATION_NFA: tuple[int, int] = ((0,1), (0,2), (1,3), (2,4), (3,5), (4,5))
KLENEE_CLOSURE_NFA: tuple[int, int] = ((0,1), (0,3), (1,2), (2,3), (3,0))
CONCATINATION_NFA: tuple[int, int] = ((0,1), (1,2), (2,3))