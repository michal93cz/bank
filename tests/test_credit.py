import unittest
from bank import Bank
from investment import Investment
from bank_account import BankAccount
from credit import Credit
import random


class TestCredit(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.USER_ID = random.randint(1, 10)
        self.ACCOUNT_ID = random.randint(1, 10)
        self.CREDIT_ID = random.randint(11, 20)

    def test_make_credit(self):
        # Create new account
        account = self.bank.makeAccount(self.USER_ID, self.ACCOUNT_ID)
        credit = self.bank.makeCredit(200, account, self.ACCOUNT_ID, self.USER_ID, self.CREDIT_ID)
        user_credits = self.bank.getUserCredits(self.USER_ID)

        # Check is user has only one credit
        self.assertEqual(len(user_credits), 1)

        # Check is it the same which return bank
        self.assertEqual(credit, user_credits[0])



