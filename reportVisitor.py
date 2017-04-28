from credit import Credit
from investment import Investment
from bank_account import BankAccount

class ReportVisitor:
    def visitCredit(self, credit):
        pass

    def visitInvestment(self, investment):
        pass

    def visitBankAccount(self, bankAccount):
        pass
