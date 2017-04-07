from Command import command
from bank_account import BankAccount


class Deposit(command):

    def __init__(self, b: BankAccount):
        self.bank_account = b

    def execute(self):
        pass

