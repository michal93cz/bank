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

    # Wydaje mi się, że taki test nie ma sensu i jest trochę na siłę, bo tak naprawdę sprawdzamy
    # czy w Pythonie działa operacja przypisania wartości do zmiennej

    # jest to tak naprawde test konstruktora, jesli ktoś w przyszłości zmieniłby jego działanie
    # to powinien się wysypać i po to własnie jest
    def test_empty_get_clients(self):
        self.assertEqual(self.newBank.getClients(), [])

    def test_empty_get_products(self):
        self.assertEqual(self.newBank.getProducts(), [])

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
        investment = self.newBank.makeInvestment(3, 45, 3, self.USER_ID, self.PRODUCT_ID_2)
        self.assertNotEqual(self.newBank.getUserInvestments(self.USER_ID)[0], account)
        self.assertEqual(self.newBank.getUserInvestments(self.USER_ID)[0], investment)
