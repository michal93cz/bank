from credit import Credit
from investment import Investment
from bank_account import BankAccount
from visitor import Visitor


# Check is product has more than 500 money
class CashLimitVisitor(Visitor):
    # todo: dopisać metody raportowania
    def visit_credit(self, credit: Credit):
        print('visit credit')
        if credit.getBalance() >= 500:
            return credit
        else:
            return None

    def visit_investment(self, investment: Investment):
        print('visit investment')
        if investment.getBalance() >= 500:
            return investment
        else:
            return None
        pass

    def visit_bank_account(self, bank_account: BankAccount):
        print('visit account')
        if bank_account.getBalance() >= 500 and bank_account.debit.get_current_debit() >= 0:
            return bank_account
        else:
            return None
        pass

