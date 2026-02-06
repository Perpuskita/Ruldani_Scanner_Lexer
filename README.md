# Ruldani_Scanner_Lexer

Ruldani scanner lexer adalah project chain dari [ruldani visual programming](https://github.com/Perpuskita/Ruldani_VisualProgramming). Ruldani scanner lexer adalah tools untuk melakukan lexical analysis dengan pendekatan finite automata. 

# Tujuan
Tujuan dari project ini adalah untuk mempelajari teori automata, mengenal teori compiler, mempelajari tahapan lexical analysis serta sebagai tools pengembangan untuk ruldani visual programming.


# Roadmap

| Fitur | Deskripsi | Status |
|-------|-------------|----------|
| RE Printing   | Melakukan printing posibility terhadap reguler expression   | ✅ complete   |
| RE Validate   | Melakukan validasi token menggunakan reguler expression | ✍🏽 development   |
| NFA Visualized   | Memvisualisasikan NFA | ✍🏽 development   |
| DFA Visualized   | Memvisualisasikan DFA | ✍🏽 development   |
| RE to NFA   | Mengkonversi RE kedalam bentuk NFA | ✍🏽 development   |
| NFA to DFA   | Mengkonversi NFA kedalam bentuk DFA | ✍🏽 development   |
| RE to DFA   | Mengkonversi RE kedalam bentuk DFA | ✍🏽 development   |

# Teknik konversi
graph LR
    A[Reguler Expression] -->|Thompson Constructions| B[Non-Deterministic Finite Automata] -->|Subset Constructions| C[Deterministic Finite Automata]

graph TD
    A[Atas] --> B[Bawah]
    style A fill:#f9f
    style B fill:#bbf
