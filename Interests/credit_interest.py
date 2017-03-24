from Interests.interest import Interest


class CreditInterest(Interest):
    def __init__(self):
        self._interests = 3

    def get_interests_value(self, money):
        return self._interests/100 * money
