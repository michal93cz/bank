from bank_account_component import BankAccountComponent
from bank_product import BankProduct
from history import History
from visitor import Visitor


class BankAccount(BankProduct, BankAccountComponent):
    def __init__(self, bank_id: int, user_id: int, product_id: int):
        self._account_balance = 0
        BankProduct.__init__(self, bank_id = bank_id, user_id=user_id, product_id=product_id, type='account')
        self._history.append(History("Account opened", self.getId()))

    def close_product(self):
        self._history.append(History("Account closed", self.getId()))
        return True

    def get_account_balance(self):
        return self._account_balance

    def _set_account_balance(self, value):
        self._account_balance = value

    def withdraw(self, money, transfer=False):
        if money > self._account_balance:
            print('Not enough money for withdraw.')
            return 0
        if money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return 0
        self._account_balance -= money
        if not transfer:
            self._history.append(History('Withdraw ' + str(money), self.getId()))
        return money

    def deposit(self, money, transfer=False):
        print('Deposit ' + str(money))
        if not transfer:
            self._history.append(History('Deposit ' + str(money), self.getId()))
        self._account_balance += money
        return money

    def pay_interest(self, value):
        if value > self._account_balance + (self.debit.get_max_debit()-self.debit.get_current_debit()):
            print('Not enough money to pay interest.')
            return False
        if value <= 0:
            print('Interest value must be greater than zero')
            return False
        self._account_balance -= value
        return True

    def addToHistory(self,h:History):
        self.bank_account._history.append(h)

    def get_bank_id(self):
        return self._bank_id

    def accept(self, visitor):
        return visitor.visit_bank_account(self)

