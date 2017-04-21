from Command import command
from bank_account import BankAccount

class BetweenBankTransfer(command):

    def __init__(self, b: BankAccount, money):
        self.bank_account = b
        self.money = money

    def execute(self):
        pass