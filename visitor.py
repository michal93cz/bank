from credit import Credit
from investment import Investment
from bank_account import BankAccount
from reportVisitor import ReportVisitor

class Visitor:
    def visit(self, element):
        if(isinstance(element, Credit)):
            self.visitCredit(element)
        elif(isinstance(element, Investment)):
            self.visitInvestment(element)
        elif(isinstance(element, BankAccount)):
            self.visit(element)

    def visitCredit(self, credit):
        pass

    def visitInvestment(self, investment):
        pass

    def visitBankAccount(self, bankAccount):
        pass

