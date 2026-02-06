class lexical_error:
    def __init__(self):
        pass

    def minimum_klenee_closure_exception(self):
        return "klenee closure tidak valid karena jumlah kurang dari 2"

    def none_variable_klenee_closure_exception(self):
        return "klenee closure tidak valid karena terdapat none variabel"

    def none_variabel_alternation_exception(self):
        return "alternation tidak valid karena terdapat none variabel"

    def none_variabel_concatination_exception(self):
        return "concatination tidak valid karena terdapat none variabel"

    def maximum_render_exception(self):
        return "expressi tidak dapat dirender sebanyak itu"