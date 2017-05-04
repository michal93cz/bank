from Interests.interest import Interest
from bank_product import BankProduct


class AccountInterestB(Interest):
    def get_interests_value(self, product: BankProduct):
        money = product.getBalance()

        if money < 10000:
            return money * 0.03
        elif money < 50000:
            return money * 0.02
        else:
            return money * 0.01
