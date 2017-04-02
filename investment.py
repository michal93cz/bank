#Lokata
from bank_product import BankProduct
import time
from history import History


class Investment(BankProduct):
    def __init__(self, endDate, amount, account, interest, user_id, product_id):
        self._starting_date = time.asctime(time.localtime(time.time()))
        self._ending_date = endDate
        self._account = account
        self._account.withdraw(amount)
        self._investment_amount = amount
        self._interest = interest
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='investment')
        self._history.append(History("Investment started with value: "+str(amount), self.getId()))

    def interest_for_date(self, date):
        return self._investment_amount * (self._interest / self._diff_month(self._starting_date, date))

    def close_product(self, date):
        if self._ending_date == date:
            self._account.deposit(self._investment_amount + self._interest * self._investment_amount)
        else:
            self._account.deposit(self._investment_amount)
        self._history.append(History("Investment closed", self.getId()))

    def _diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    def get_investment_amount(self):
        return self._investment_amount

    def get_end_date(self):
        return self._ending_date
