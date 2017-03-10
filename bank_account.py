from bank_product import BankProduct


class BankAccount(BankProduct):

    def __init__(self, userId, productId):
        self._account_balance = 0
        BankProduct.__init__(self, user_id = userId, product_id = productId)

    def close_product(self):
        pass

    def withdraw(self, money):
        if money > self._account_balance:
            print('Not enough money for withdraw')
        self._account_balance -= money
        print('Withdraw ' + str(money))
        return money

    def deposit_money(self, money):
        print('Deposit ' + str(money))
        self._account_balance += money

    def current_account_balance(self):
        print('Current account balance is ' + str(self._account_balance))
        return self._account_balance
