from Operations.operation import Operation
from bank_account import BankAccount


class Deposit(Operation):
    def __init__(self, account_to: BankAccount, money):
        self.account_to = account_to
        self.money = money

    def execute(self):
        print('Deposit ' + str(self.money))
        # self._history.append(History('Deposit ' + str(money), self.getId()))
        rest = self.account_to.debit.cut_debit(self.money)
        self.account_to.add(rest)
