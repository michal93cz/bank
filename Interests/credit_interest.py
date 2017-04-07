from Interests.interest import Interest


class CreditInterest(Interest):

    def __init__(self, percent):
        Interest.__init__(self, percent)

    def get_interests_value(self, money):
        return self.percent/100 * money

