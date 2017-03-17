#Lokata
from bank_product import BankProduct


class Investment(BankProduct):

    def __init__(self, date, amount, interest, user_id, product_id):
        self._starting_date = date
        self._investment_amount = amount
        self._interest = interest
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='investment')

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
