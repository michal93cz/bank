from Interests.interest import Interest
from bank_product import BankProduct


class InvestmentInterest(Interest):
    def get_interests_value(self, product: BankProduct):
        return 0.03 * product.getBalance()
