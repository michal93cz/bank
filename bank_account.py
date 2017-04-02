from bank_product import BankProduct
from debit import Debit
from history import History


class BankAccount(BankProduct):
    def __init__(self, user_id, product_id, debit=50):
        self._account_balance = 0
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='account')
        self.debit = Debit(debit)
        self._history.append(History("Account opened", self.getId()))

    def close_product(self):
        if self.debit.get_current_debit() > 0:
            print("You can't close account until your debit is not equal 0")
            return False
        self._history.append(History("Account closed", self.getId()))
        return True

    def get_account_balance(self):
        return self._account_balance

    def withdraw(self, money, transfer=False):
        if money > self._account_balance + (self.debit.get_max_debit()-self.debit.get_current_debit()):
            print('Not enough money for withdraw.')
            return 0
        if money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return 0
        self._account_balance -= money
        if self._account_balance < 0:
            self.debit.extend_debit(self._account_balance*(-1))
            self._account_balance = 0
        if not transfer:
            self._history.append(History('Withdraw ' + str(money), self.getId()))
        return money

    def deposit(self, money, transfer=False):
        print('Deposit ' + str(money))
        if not transfer:
            self._history.append(History('Deposit ' + str(money), self.getId()))
        rest = self.debit.cut_debit(money)
        self._account_balance += rest
        return money

    def current_account_balance(self):
        print('Current account balance is ' + str(self._account_balance-self.debit.get_current_debit()))
        return self._account_balance-self.debit.get_current_debit()

    def pay_interest(self, value):
        if value > self._account_balance + (self.debit.get_max_debit()-self.debit.get_current_debit()):
            print('Not enough money to pay interest.')
            return False
        if value <= 0:
            print('Interest value must be greater than zero')
            return False
        self._account_balance -= value
        return True
