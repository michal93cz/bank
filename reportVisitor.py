from credit import Credit
from investment import Investment
from bank_account import BankAccount


class ReportVisitor:
    # todo: dopisać metody raportowania
    def visit_credit(self, credit: Credit):
        pass

    def visit_investment(self, investment: Investment):
        pass

    def visit_bank_account(self, bank_account: BankAccount):
        pass

