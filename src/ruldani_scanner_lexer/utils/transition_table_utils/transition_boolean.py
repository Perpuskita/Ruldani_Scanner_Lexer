
"""
menampung boolean dari transisi di transition function
transition boolean berjumlah input * state
"""
class transition_boolean:
    def __init__(self):
        self.transition_boolean_list = []
        pass

    def add_transition(self, trans_state: str) -> bool:
        for trans in self.transition_boolean_list :
            if trans == trans_state :
                return False
        self.transition_boolean_list.append(trans_state)
        return True
    
    def get_transition(self) -> list :
        hasil: str = ""
        for trans in self.transition_boolean_list:
            hasil += trans + " "
        return hasil
