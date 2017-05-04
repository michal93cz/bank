from Interests.interest import Interest


class AccountInterestB(Interest):
    def __init__(self, b):
        Interest.__init__(self, b)

    def get_interests_value(self, money):
        if money < 10000:
            return money * 0.03
        elif money < 50000:
            return money * 0.02
        else:
            return money * 0.01
