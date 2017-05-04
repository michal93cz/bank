from Interests.interest import Interest


class CreditInterest(Interest):

    def __init__(self, b):
        Interest.__init__(self, b)
        self._percent = 3

    def get_interests_value(self):
        return self.percent/100 * self.product.getBalance()

