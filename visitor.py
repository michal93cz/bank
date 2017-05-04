from credit import Credit
from investment import Investment


class Visitor:
    def visit(self, element):
        #important import! here to avoid cycle import
        import bank_account
        if isinstance(element, Credit):
            self.visit_credit(element)
        elif isinstance(element, Investment):
            self.visitInvestment(element)
        elif isinstance(element, bank_account.BankAccount):
            self.visitBankAccount(element)

    def visit_credit(self, credit):
        pass

    def visit_investment(self, investment):
        pass

    def visit_bank_account(self, bank_account):
        pass

