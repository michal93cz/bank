from Interests.interest import Interest


class CreditInterest(Interest):
    @staticmethod
    def get_interests_value(self, money):
        return 0.01 * money
