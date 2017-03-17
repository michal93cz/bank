from bank_account import BankAccount
from credit import Credit
from investment import Investment
import time


class Interest:
    def __init__(self, product, interest=3):
        self._product = product
        self._interests = interest

    def _credit_interest(self):
        # TODO: ogarnąć porównywanie dat (to jest atrapa)
        if self._product.get_end_date < time.asctime(time.localtime(time.time())):
            self._interests += 3# karne oprocentowanie za opóźnienie
        return (self._interests/100.0) * self._product.get_credit_value()

    def _investment_interest(self):
        # TODO: ogarnąć porównywanie dat (to jest atrapa)
        if self._product.get_end_date > time.asctime(time.localtime(time.time())):
            return 0
        return self._product.get_investment_amount * (self._interests/100.0)

    def get_interests_value(self):
        if type(self._product) is BankAccount:
            return self._product.debit.get_current_debit() * (self._interests/100.0)
        if type(self._product) is Credit:
            return self._credit_interest()
        if type(self._product) is Investment:
            return self._investment_interest()
