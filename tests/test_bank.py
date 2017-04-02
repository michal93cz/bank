import unittest
from bank import Bank
from investment import Investment
from bank_account import BankAccount
from credit import Credit


class TestBank(unittest.TestCase):
    def setUp(self):
        self.newBank = Bank()
        self.USER_ID = 3
        self.SECOND_USER_ID = 2
        self.PRODUCT_ID = 5
        self.PRODUCT_ID_2 = 7

    def test_empty_get_clients(self):
        self.assertEqual(self.newBank.getClients(), [])

    def test_empty_get_products(self):
        self.assertEqual(self.newBank.getProducts(), [])

    def test_empty_get_raports(self):
        self.assertEqual(self.newBank.getRaports(), [])

    def test_make_client(self):
        self.newBank.makeClient(self.USER_ID)
        self.assertEqual(self.newBank.getClients()[0], self.USER_ID)

    def test_make_account(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        self.assertEqual(type(self.newBank.getProducts()[0]), BankAccount)
        self.assertEqual(self.newBank.getProducts()[0], account)

    def test_make_investment(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account.deposit(100)
        self.assertEqual(account.current_account_balance(), 100)
        investment = self.newBank.makeInvestment(3, 45, account, 3, self.USER_ID, self.PRODUCT_ID_2)
        self.assertEqual(account.current_account_balance(), 100 - 45)
        self.assertEqual(type(self.newBank.getProducts()[1]), Investment)
        self.assertEqual(self.newBank.getProducts()[1], investment)

    def test_make_credit(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        account.deposit(100)
        credit = self.newBank.makeCredit(200, account, 3, self.USER_ID, self.PRODUCT_ID_2)
        self.assertEqual(account.current_account_balance(), 100 + 200)
        self.assertEqual(type(self.newBank.getProducts()[1]), Credit)
        self.assertEqual(self.newBank.getProducts()[1], credit)

    def test_get_user_products(self):
        self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID_2)
        self.assertNotEqual(len(self.newBank.getUserProducts(self.USER_ID)), 5)
        self.assertNotEqual(len(self.newBank.getUserProducts(self.USER_ID)), 1)
        self.assertEqual(len(self.newBank.getUserProducts(self.USER_ID)), 2)

    def test_get_user_product(self):
        self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        product = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID_2)
        self.assertNotEqual(self.newBank.getUserProduct(self.USER_ID, self.PRODUCT_ID), product)
        self.assertEqual(self.newBank.getUserProduct(self.USER_ID, self.PRODUCT_ID_2), product)

    def test_get_user_accounts(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        credit = self.newBank.makeCredit(3, account, 3, self.USER_ID, self.PRODUCT_ID_2)
        self.assertNotEqual(self.newBank.getUserAccounts(self.USER_ID)[0], credit)
        self.assertEqual(self.newBank.getUserAccounts(self.USER_ID)[0], account)

    def test_get_user_credits(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        credit = self.newBank.makeCredit(3, account, 3, self.USER_ID, self.PRODUCT_ID_2)
        self.assertNotEqual(self.newBank.getUserCredits(self.USER_ID)[0], account)
        self.assertEqual(self.newBank.getUserCredits(self.USER_ID)[0], credit)

    def test_get_user_investments(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        investment = self.newBank.makeInvestment(3, 45, account, 3, self.USER_ID, self.PRODUCT_ID_2)
        self.assertNotEqual(self.newBank.getUserInvestments(self.USER_ID)[0], account)
        self.assertEqual(self.newBank.getUserInvestments(self.USER_ID)[0], investment)

    def test_transfer(self):
        first_account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        second_account = self.newBank.makeAccount(self.SECOND_USER_ID, self.PRODUCT_ID_2)
        money = 1024
        first_account.deposit(money)
        self.assertEqual(self.newBank.transfer(first_account, second_account, money), True)
        self.assertEqual(first_account.current_account_balance(), 0)
        self.assertEqual(second_account.current_account_balance(), 1024)
