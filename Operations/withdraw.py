from Operations.operation import Operation
from bank_account import BankAccount
from history import History


class Withdraw(Operation):
    def __init__(self, account_from: BankAccount, money):
        self.account_from = account_from
        self.money = money

    def execute(self):
        if self.money > self.account_from.getBalance() + (self.account_from.debit.get_max_debit()-self.account_from.debit.get_current_debit()):
            print('Not enough money for withdraw.')
            return 0
        if self.money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return 0
        self.account_from.subtract(self.money)
        if self.account_from.getBalance() < 0:
            self.account_from.debit.extend_debit(self._account_balance*(-1))
        self.account_from.addToHistory(History('Withdraw ' + str(self.money), self.getId()))
