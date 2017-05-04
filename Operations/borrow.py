from Operations.operation import Operation
from bank_account_component import BankAccountComponent


class Borrow(Operation):
    def __init__(self, account_to: BankAccountComponent, money):
        self.account_to = account_to
        self.money = money

    def execute(self):
        print('Borrow ' + str(self.money))
        self.account_to.add(self.money)
