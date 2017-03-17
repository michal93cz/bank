from bank_product import BankProduct
import time


class Credit(BankProduct):
    def __init__(self, money, account, end_date, user_id, product_id):
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='credit')
        self._money = money
        self._account = account
        self._begin_date = time.asctime(time.localtime(time.time()))
        self._end_date = end_date
        account.deposit_money(money)

    def close_product(self, interests):
        to_pay = self.money+(self.money*interests)
        payed = self._account.withdraw(to_pay)
        if (payed is not None) and (payed == to_pay):
            print("Kredyt spłacony")
            return True
        else:
            print("Brak wystarczających środków do spłaty kredytu")
            return False


    def get_credit_value(self):
        return self._money

    def get_account(self):
        return self._account

    def get_begin_date(self):
        return self._begin_date

    def get_end_date(self):
        return self._end_date
