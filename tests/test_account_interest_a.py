import unittest
from Interests.account_interest_b import AccountInterestB
from bank_account import BankAccount


class AccountInterestATestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1, 2, 50)

    def smallValue(self):
        self.account.deposit(500)

    def mediumValue(self):
        self.account.deposit(2500)

    def largeValue(self):
        self.account.deposit(10000)

