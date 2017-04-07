from Interests.interest import Interest
from bank_product import BankProduct


class AccountInterestC(Interest):

    def __init__(self, b: BankProduct):
        Interest.__init__(self, b)

    def get_interests_value(self):
        money = self.product.getBalance()
        if money < 10000:
            percent = 0.01
        elif money < 300000:
            percent = 0.04
        else:
            percent = 0.02
        return money * percent

