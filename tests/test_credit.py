import unittest
from bank import Bank
import random
from Interests import credit_interest


class TestCredit(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.USER_ID = random.randint(1, 10)
        self.ACCOUNT_ID = random.randint(1, 10)
        self.CREDIT_ID = random.randint(11, 20)
        self.account = self.bank.makeAccount(self.USER_ID, self.ACCOUNT_ID)
        self._number_of_installment = 12

    def test_make_credit(self):
        # Create new account
        credit = self.bank.makeCredit(200, self.account, self.ACCOUNT_ID, self.USER_ID, self.CREDIT_ID, self._number_of_installment)
        user_credits = self.bank.getUserCredits(self.USER_ID)

        # Check is user has only one credit
        self.assertEqual(len(user_credits), 1)

        # Check is it the same which return bank
        self.assertEqual(credit, user_credits[0])

    def test_attempt_to_repay_credit(self):
        self.account.deposit(100)
        number_of_installment = 12
        credit = self.bank.makeCredit(200, self.account, self.ACCOUNT_ID, self.USER_ID, self.CREDIT_ID, number_of_installment)

        for i in range(0, credit._number_of_installment):
            credit.pay_one_installment()

        self.assertEqual(300 - ((200 * 0.05) + 200), self.account.get_account_balance())

    def test_make_credit_with_incorrect_values(self):
        try:
            self.bank.makeCredit(-200, self.account, self.ACCOUNT_ID, self.USER_ID, self.CREDIT_ID, self._number_of_installment)
        except ValueError:
            pass
        else:
            self.fail('ValueError exception not except')





