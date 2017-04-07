from Command import command
from bank_account import BankAccount
from history import History


class Withdraw(command):

    def __init__(self, b: BankAccount, money):
        self.bank_account = b
        self.money = money

    def execute(self):
        if self.money > self.bank_account.getBalance() + (self.bank_account.debit.get_max_debit()-self.bank_account.debit.get_current_debit()):
            print('Not enough money for withdraw.')
            return 0
        if self.money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return 0
        self.bank_account._set_account_balance(self.bank_account.getBalance() - self.money)
        if self.bank_account.getBalance() < 0:
            self.bank_account.debit.extend_debit(self._account_balance*(-1))
        self.bank_account.addToHistory(History('Withdraw ' + str(self.money), self.getId()))


