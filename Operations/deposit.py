from Operations.operation import Operation
from bank_account import BankAccount
from bank_account_component import BankAccountComponent


class Deposit(Operation):
    def __init__(self, account_to: BankAccountComponent, money):
        self.account_to = account_to
        self.money = money

    def execute(self):
        print('Deposit ' + str(self.money))
        # self._history.append(History('Deposit ' + str(money), self.getId()))
        self.account_to.add(self.money)
