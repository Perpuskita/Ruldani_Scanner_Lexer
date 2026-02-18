class lexical_error:
    def __init__(self):
        pass

    def minimum_klenee_closure_exception(self) -> str:
        return "klenee closure tidak valid karena jumlah kurang dari 2"

    def none_variable_klenee_closure_exception(self) -> str:
        return "klenee closure tidak valid karena terdapat none variabel"

    def none_variabel_alternation_exception(self)-> str:
        return "alternation tidak valid karena terdapat none variabel"

    def none_variabel_concatination_exception(self) -> str:
        return "concatination tidak valid karena terdapat none variabel"

    def maximum_render_exception(self) -> str:
        return "expressi tidak dapat dirender sebanyak itu"

class transition_table_error:
    def __init__(self):
        pass

    def undifined_argument(self, nama: str) -> int:
        print(f"undefined argument {nama}")
        return -1

    def uncomplete_assign(self) -> str :
        return None


class nondeterministic_finite_automata_error:
    def __init__ (self):
        pass

    def undefined_start_state(self):
        return f"start state tidak ditemukan"

    def disconnected_state(self, massage: str) -> str:
        return f"state tidak terhubung dengan state lain"

    def undefined_start_state(self, massage: str) -> str:
        return f"error stat state tidak didefinisikan {massage}"
    
