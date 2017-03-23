class BankOperations:
    @staticmethod
    def transfer(accountFrom, accountTo, amount):
        if accountFrom.withdraw(amount):
            accountTo.deposit_money(amount)

    @staticmethod
    def deposit(accountFrom, accountTo, amount):
        if accountFrom.withdraw(amount):
            accountTo.deposit_money(amount)
