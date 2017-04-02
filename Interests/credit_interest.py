from Interests.interest import Interest


class CreditInterest(Interest):

    def __init__(self, value, percent):
        Interest.__init__(self, value, percent)

    def get_interests_value(self, money):
        return self.percent/100 * money

