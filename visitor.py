from credit import Credit
from investment import Investment
from bank_account import BankAccount
from reportVisitor import ReportVisitor

class Visitor:
    def visit(self, element):
        if isinstance(element, Credit):
            self.visit_credit(element)
        elif isinstance(element, Investment):
            self.visitInvestment(element)
        elif isinstance(element, BankAccount):
            self.visitBankAccount(element)

    def visit_credit(self, credit: Credit):
        pass

    def visit_investment(self, investment: Investment):
        pass

    def visit_bank_account(self, bank_account: BankAccount):
        pass

