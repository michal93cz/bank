from Interests.interest import Interest


class AccountInterestA(Interest):
    def __init__(self, b):
        Interest.__init__(self, b)

    def get_interests_value(self):
        money = self.product.getBalance()

        if money < 1000:
            percent = 0.02
        elif money < 3000:
            percent = 0.05
        else:
            percent = 0.1
        return money * percent

