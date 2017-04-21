import random
import unittest
from bank import Bank
from investment import Investment


class TestInvestment(unittest.TestCase):
    def setUp(self):
        self.bank_id = 1
        self.bank = Bank(bank_id=self.bank_id)
        self.USER_ID = random.randint(1, 10)
        self.ACCOUNT_ID = random.randint(1, 10)
        self.INVESTMENT_ID = random.randint(11, 20)
        self.account = self.bank.makeAccount(self.USER_ID, self.ACCOUNT_ID)

    def test_make_investment(self):
        self.account.deposit(100)
        investment = self.bank.makeInvestment(3, 45, self.account, 3, self.USER_ID, self.INVESTMENT_ID)
        self.assertEqual(self.account.current_account_balance(), 100 - 45)
        self.assertEqual(len(self.bank.getUserInvestments(self.USER_ID)), 1)
        self.assertEqual(type(self.bank.getProducts()[1]), Investment)
        self.assertEqual(self.bank.getProducts()[1], investment)

    def test_make_negative_investment(self):
        try:
            self.bank.makeInvestment(3, -45, self.account, 3, self.USER_ID, self.INVESTMENT_ID)
        except ValueError:
            pass
        else:
            self.fail("Value error not raised")

    def test_investment_with_close(self):
        account_value = 100
        investment_value = 100
        interest = 0.3
        self.account.deposit(account_value)
        investment = self.bank.makeInvestment('02-04-2017', investment_value, self.account, interest, self.USER_ID, self.INVESTMENT_ID)
        investment.close_product('02-04-2017')
        self.assertEqual(self.account.get_account_balance(), account_value + investment_value * interest)


