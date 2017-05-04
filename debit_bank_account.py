from bank_account import BankAccount
from bank_account_component import BankAccountComponent
from bank_product import BankProduct
from debit import Debit


class DebitBankAccount(BankProduct, BankAccountComponent):
    def __init__(self, bank_account: BankAccount, max_debit=50):
        self.bank_account = bank_account
        self.debit = Debit(max_debit)

    def get_account_balance(self):
        return self.bank_account.get_account_balance()-self.debit.get_current_debit();

    def withdraw(self, money, transfer=False):
        if money > self.bank_account.get_account_balance() + (self.debit.get_max_debit()-self.debit.get_current_debit()):
            print('Not enough money for withdraw.')
            return 0
        if money < 1:
            print('Money which you want to withdraw must be greater than zero!')
            return 0

        to_debit = 0
        if self.bank_account.get_account_balance() - money < 0:
            to_debit = money - self.bank_account.get_account_balance()
            self.debit.extend_debit(to_debit)
            money -= to_debit

        if self.bank_account.withdraw(money, transfer) == money:
            return money + to_debit

        print('internal error in debit account withdraw');
        return 0

    def deposit(self, money, transfer=False):
        print('Deposit in debit account ' + str(money))
        current_debit = self.debit.get_current_debit()
        rest = self.debit.cut_debit(money)
        return self.bank_account.deposit(rest, transfer)+current_debit

    # przesłonięte metody z BankProduct
    def close_product(self):
        if self.debit.get_current_debit() > 0:
            print("You can't close account until your debit is not equal 0")
            return False
        return self.bank_account.close_product()

    def getOwner(self):
        return self.bank_account.getOwner()

    def get_bank_id(self):
        return self.bank_account.get_bank_id()

    def getId(self):
        return self.bank_account.getId()

    def getOwner(self):
        return self.bank_account.getOwner()

    def getHistory(self):
        return self.bank_account.getHistory()
