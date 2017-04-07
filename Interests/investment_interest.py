from Interests.interest import Interest


class InvestmentInterest(Interest):
    def get_interests_value(self, money):
        return 0.01 * money
