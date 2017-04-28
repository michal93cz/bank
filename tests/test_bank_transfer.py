import unittest
from bank import Bank
from kir import Kir

class TestBankTransfer(unittest.TestCase):
    def setUp(self):
        kir = Kir()
        self.first_bank = Bank(1)
        kir.add_bank(self.first_bank)

        self.second_bank = Bank(2)
        kir.add_bank(self.second_bank)

        first_client_id = 1
        second_client_id = 2
        first_bank_client = self.first_bank.makeClient(first_client_id)
        second_bank_client = self.second_bank.makeClient(second_client_id)
        self.first_bank_client_account = self.first_bank.makeAccount(first_client_id, 3)
        self.second_bank_client_account = self.second_bank.makeAccount(second_client_id, 4)

    def test_transfer_to_another_bank(self):
        money = 100
        first_client_money = self.first_bank_client_account.get_account_balance();
        second_client_money = self.second_bank_client_account.get_account_balance();
        self.first_bank_client_account.deposit(money)
        result = self.first_bank.transfer(self.first_bank_client_account, self.second_bank_client_account, money)
        self.assertEqual(result, True, "Transfer error")
        self.assertEqual(self.first_bank_client_account.getBalance(), first_client_money, "First client still have a money")
        self.assertEqual(self.second_bank_client_account.getBalance(), (second_client_money+money))

    def test_rollback(self):
        money = 1000
        self.first_bank_client_account.deposit(money)
        self.second_bank_client_account.close_product()
        result = self.first_bank.transfer(self.first_bank_client_account, self.second_bank_client_account, money)
        self.assertEqual(result, False, "Transfer should't be done")
        self.assertEqual(self.first_bank_client_account.getBalance(), money, "First client should still have a money")