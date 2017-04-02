from Interests.interest import Interest


class InvestmentInterest(Interest):
    def __init__(self, value, percent):
        Interest.__init__(self, value, percent)

    def get_interests_value(self, money):
        return self._interests/100 * money
