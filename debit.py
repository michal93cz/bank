# określa warunki debetu
# egzekwuje spłatę debetu


class Debit:
    def __init__(self, max_value):
        self._max_debit_value = max_value
        self._current_debit_value = 0

    def set_max_debit(self, max_debit_value):
        self._max_debit_value = max_debit_value

    def get_max_debit(self):
        return self._max_debit_value

    def print_max_debit(self):
        print("Maximum debit for this bank product: ", self._max_debit_value)

    def get_current_debit(self):
        return self._current_debit_value

    def print_current_debit(self):
        print("Current debit: ", self._current_debit_value)

    def extend_debit(self, value):
        if self._current_debit_value + value <= self._max_debit_value:
            self._current_debit_value += value
            self.print_current_debit()
            return 0
        else:
            print("Cannot extend your debit. Current debit: ", self._current_debit_value)
            return 1

    def cut_debit(self, value):
        self._current_debit_value -= value
        if self._current_debit_value < 0:
            rest = -self._current_debit_value
            self._current_debit_value = 0
            self.print_current_debit()
            return rest
        else:
            self.print_current_debit()
            return 0
