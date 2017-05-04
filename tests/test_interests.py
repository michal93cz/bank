import unittest
from Interests.account_interest_a import AccountInterestA
from Interests.account_interest_b import AccountInterestB
from Interests.account_interest_c import AccountInterestC
from bank_account import BankAccount


class AccountInterestBTestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(32, 45)


    def test_get_default_interests(self):
        self.account.deposit(100)
        self.account.getInterests()

        self.assertEqual(self.account.getInterests(), 100 + 0.02 * 100)

    # def test_set_B_interest(self):
    #     accountInterestB = AccountInterestB()
    #     self.account.setInterest(accountInterestB)
