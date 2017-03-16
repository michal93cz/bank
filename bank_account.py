from bank_product import BankProduct
from debit import Debit


class BankAccount(BankProduct):
    def __init__(self, user_id, product_id, debit=50):
        self._account_balance = 0
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='account')
        self.debit = Debit(debit)

    def close_product(self):
        if self.debit.get_current_debit() > 0:
            print("You can't close account until your debit is not equal 0")

    def withdraw(self, money):
        if money > self._account_balance + (self.debit.get_max_debit()-self.debit.get_current_debit()):
            print('Not enough money for withdraw.')
            return
        if money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return
        self._account_balance -= money
        if self._account_balance < 0:
            self.debit.extend_debit(self._account_balance*(-1))
            self._account_balance = 0
        print('Withdraw ' + str(money))
        return money

    def deposit_money(self, money):
        print('Deposit ' + str(money))
        rest = self.debit.cut_debit(money)
        self._account_balance += rest
        return money

    def current_account_balance(self):
        print('Current account balance is ' + str(self._account_balance-self.debit.get_current_debit()))
        return self._account_balance-self.debit.get_current_debit()
