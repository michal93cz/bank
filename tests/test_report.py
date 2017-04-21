import unittest
from report import Report
from bank import Bank


class DebitTestCase(unittest.TestCase):
    def setUp(self):
        self.report = Report()
        self.bank_id = 1
        self.bank = Bank(bank_id=self.bank_id)
        self.USER_ID = 3
        self.SECOND_USER_ID = 2
        self.PRODUCT_ID = 5
        self.PRODUCT_ID_2 = 7

    def test_sum_of_founds_in_bank(self):
        self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID).deposit(200)
        self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID).deposit(300)

        self.assertEqual(self.report.sum_of_founds_in_bank(self.newBank.getProducts()), 200 + 300)

    def test_sum_of_founds_in_bank_with_credit(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account.deposit(200)
        self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID).deposit(300)
        self.newBank.makeCredit(500, account, 4, self.USER_ID, 3567)

        self.assertEqual(self.report.sum_of_founds_in_bank(self.newBank.getProducts()), 200 + 300 + 500)

    def test_sum_of_debits(self):
        account1 = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account1.deposit(200)
        account1.withdraw(230)
        account2 = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account2.deposit(300)
        account2.withdraw(340)

        self.assertEqual(self.report.sum_of_debits(self.newBank.getProducts()), 30 + 40)

    def test_sum_of_debits_with_investments(self):
        account1 = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account1.deposit(200)
        account2 = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account2.deposit(300)
        account2.withdraw(340)
        self.newBank.makeInvestment(32, 230, account1, 3, self.USER_ID, 3567)

        self.assertEqual(self.report.sum_of_debits(self.newBank.getProducts()), 30 + 40)
