from Operations.operation import Operation
from bank_account import BankAccount

class ReverseBankTransfer(Operation):

    def __init__(self, b: BankAccount, money):
        self.bank_account = b
        self.money = money

    def execute(self):
        pass