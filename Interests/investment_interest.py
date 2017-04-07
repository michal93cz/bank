from Interests.interest import Interest
from bank_product import BankProduct


class InvestmentInterest(Interest):
    def __init__(self, b: BankProduct):
        Interest.__init__(self, b)
        self_percent = 3

    def get_interests_value(self):
        return self.percent/100 * self.product.getBalance()
