import unittest
from bank_account import BankAccount
from debit_bank_account import DebitBankAccount


class BankAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account = DebitBankAccount(BankAccount(1, 2, 1))

    def test_close_product_without_founds(self):
        self.assertEqual(self.account.close_product(), True, 'Cannot close account without money')

    def test_close_product_with_debit(self):
        self.account.subtract(25)
        self.assertEqual(self.account.close_product(), False, 'Closing account with debit')

    def test_close_product_with_founds(self):
        self.account.add(100)
        self.assertEqual(self.account.close_product(), True, 'Cannot close account with money')

    def test_withdraw_twenty_five_from_empty_account(self):
        money = 25
        result = self.account.subtract(money)
        self.assertEqual(result, True)
        self.assertEqual(self.account.get_account_balance(), -money)

    def test_withdraw_sixty_from_empty_account(self):
        money = 60
        result = self.account.subtract(money)
        self.assertEqual(self.account.get_account_balance(), 0)
        self.assertEqual(result, 0)

    def test_withdraw_hundread_form_seventy_five(self):
        money = 100
        deposit = 75
        self.account.add(deposit)
        result = self.account.subtract(money)
        self.assertEqual(result, True)
        self.assertEqual(self.account.get_account_balance(), deposit-money)

    def test_deposit_money(self):
        money = 20
        current_balance = self.account.get_account_balance()
        self.account.add(money)
        self.assertEqual(self.account.get_account_balance(), money+current_balance)

    def test_deposit_money_with_debit(self):
        money = 20
        self.account.add(money)
        current_balance = self.account.get_account_balance()
        self.account.add(money*2)
        self.assertEqual(self.account.get_account_balance(), money*2+current_balance)
