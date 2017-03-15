from bank_product import BankProduct


class BankAccount(BankProduct):
    def __init__(self, user_id, product_id):
        self._account_balance = 0
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='account')

    def close_product(self):
        pass

    def withdraw(self, money):
        if money > self._account_balance:
            print('Not enough money for withdraw.')
            return
        if money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return
        self._account_balance -= money
        print('Withdraw ' + str(money))
        return money

    def deposit_money(self, money):
        print('Deposit ' + str(money))
        self._account_balance += money

    def current_account_balance(self):
        print('Current account balance is ' + str(self._account_balance))
        return self._account_balance
