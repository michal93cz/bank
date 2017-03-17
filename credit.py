from bank_product import BankProduct
import time


class Credit(BankProduct):
    def __init__(self, user_id, product_id, money, account, end_date):
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='credit')
        self._money = money
        self._account = account
        self._begin_date = time.asctime(time.localtime(time.time()))
        self._end_date = end_date
        account.deposit_money(money)

    def close_product(self, interests):
        self._account.withdraw(self.money+(self.money*interests))

    def get_credit_value(self):
        return self._money

    def get_account(self):
        return self._account

    def get_begin_date(self):
        return self._begin_date

    def get_end_date(self):
        return self._end_date
