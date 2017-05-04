from Operations.operation import Operation
from bank_account import BankAccount
from history import History


class Withdraw(Operation):
    def __init__(self, account_from: BankAccount, money):
        self.account_from = account_from
        self.money = money

    def execute(self):
        if self.account_from.subtract(self.money):
            self.account_from.addToHistory(History('Withdraw ' + str(self.money), self.getId()))
