#Lokata
from bank_product import BankProduct


class Investment(BankProduct):

    def __init__(self, date, amount, interest, end_date):
        self._starting_date = date
        self._investment_amount = amount
        self._interest = interest
        self._end_date = end_date

    def interest_for_date(self, date):
        return self._investment_amount * (self._interest / self._diff_month(self._starting_date, date))

    def close_product(self):
        pass

    def _diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    def get_investment_amount(self):
        return self._investment_amount

    def get_end_date(self):
        return self._end_date
