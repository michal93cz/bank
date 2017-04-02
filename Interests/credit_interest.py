from Interests.interest import Interest


class CreditInterest(Interest):

    def get_interests_value(self, money):
        return self.percent/100 * money

