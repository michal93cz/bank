from Interests.interest import Interest


class InvestmentInterest(Interest):
    def __init__(self):
        self._interests = 2

    def get_interests_value(self, money):
        return self._interests/100 * money
