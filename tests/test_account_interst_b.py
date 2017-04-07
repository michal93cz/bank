import unittest
from Interests.account_interest_b import AccountInterestB
from bank_account import BankAccount


class AccountInterestBTestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(32, 45)
        self.accountInterest = AccountInterestB(self.account)
