# określa warunki debetu
# egzekwuje spłatę debetu
# TODO: egzekwowanie wpłaty

class Debit:
    def __init__(self, maxValue):
        self.maxDebitValue = maxValue
        self.currentDebitValue = 0

    def extendDebit(self, value):
        if(self.currentDebitValue+value <= self.maxDebitValue):
            self.currentDebitValue += value
            return 0
        else:
            return 1

    def cutDebit(self, value):
        rest = self.currentDebitValue - value
        if(rest < 0):
            rest *= -1
            return rest
        else:
            return 0