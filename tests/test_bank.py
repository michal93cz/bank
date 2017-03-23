import unittest
from bank import Bank
from investment import Investment
from bank_account import BankAccount
from credit import Credit

class TestBank(unittest.TestCase):
    def setUp(self):
        self.newBank = Bank()
        self.USER_ID = 3
        self.PRODUCT_ID = 5
        self.PRODUCT_ID_2 = 7

    def test_empty_get_clients(self):
        self.assertEqual(self.newBank.getClients(), [])

    def test_empty_get_products(self):
        self.assertEqual(self.newBank.getProducts(), [])

    def test_empty_get_history(self):
        self.assertEqual(self.newBank.getHistory(), [])

    def test_empty_get_raports(self):
        self.assertEqual(self.newBank.getRaports(), [])

    def test_make_client(self):
        client = self.newBank.makeClient(self.USER_ID)
        self.assertEqual(self.newBank.getClients()[0], client)

    def test_make_account(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        self.assertEqual(type(self.newBank.getProducts()[0]), BankAccount)
        self.assertEqual(self.newBank.getProducts()[0], account)

    def test_make_investment(self):
        investment = self.newBank.makeInvestment(3, 45, 3, self.USER_ID, self.PRODUCT_ID)
        self.assertEqual(type(self.newBank.getProducts()[0]), Investment)
        self.assertEqual(self.newBank.getProducts()[0], investment)

    def test_make_credit(self):
        account = self.newBank.makeAccount(self.USER_ID, self.PRODUCT_ID)
        credit = self.newBank.makeCredit(3, account, 3, self.USER_ID, self.PRODUCT_ID_2)
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
