import unittest

from datetime import date
from bank import Bank
from bank_account import BankAccount
from credit import Credit
from investment import Investment
from Interests.investment_interest import InvestmentInterest
from cashLimitVisitor import CashLimitVisitor
from Operations.deposit import Deposit

class VisitorTestCase(unittest.TestCase):
    def setUp(self):
        self.bank_id = 1
        self.bank = Bank(bank_id=self.bank_id)
        self.products = []
        self.accounts = []
        self.credits = []
        self.investments = []
        # Prepare products
        for i in range(1, 11):
            # accounts
            account = BankAccount(bank_id=self.bank_id, user_id=1, product_id=i*10)
            account.doOperation(Deposit(account, 300 * i))
            self.accounts.append(account)
            # credits
            credit = Credit(product_id=i*20, account=account, end_date=date.today, money=100*i, user_id=1,
                            number_of_installment=12, bank_id=self.bank_id)
            self.credits.append(credit)
            # investment
            investment = Investment(endDate=date.today, amount=100 * i + 1, interest=InvestmentInterest,
                                    product_id=i*30, account=account, user_id=1, bank_id=self.bank_id)
            self.investments.append(investment)

            # prepare one collection with all products
            self.products.append(account)
            self.products.append(credit)
            self.products.append(investment)

    def test_number_of_products_which_has_more_than_500_value(self):
        result = []
        for p in self.products:
            obj = p.accept(CashLimitVisitor())
            if not (obj is None):
                result.append(obj)

        self.assertEqual(21, len(result))









