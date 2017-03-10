from bank_product import BankProduct
class BankAccount(BankProduct):
    _account_balance = 0

    def __init__(self, starting_money):
        self._account_balance = starting_money

    def create_product(self):
        pass

    def close_product(self):
        pass

    def withdraw(self, money):
        if money > self._account_balance:
            print('Not enough money for withdraw')
        self._account_balance -= money
        return money

    def deposit_money(self, money):
        self._account_balance += money

    def current_account_balance(self):
        return self._account_balance
