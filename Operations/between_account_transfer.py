from Operations.operation import Operation
from bank_account import BankAccount

class BetweenAccountTransfer(Operation):
    def __init__(self, account_from: BankAccount, account_to: BankAccount, money):
        self.account_from = account_from
        self.account_to = account_to
        self.money = money

    def execute(self):
        if self.account_from.get_bank_id() != self.account_to.get_bank_id():
            print("Przelew miedzy bankowy")
            if self.account_from.current_account_balance() < self.money:
                return False
            # result = self.kir.make_transfer(self.account_to.get_bank_id(), self.money, self.account_to.getId())
            # if result == False:
            #     return result

            self.account_from.subtract(self.money)
            self.account_to.add(self.money)
            # h_from = History("Outgoing transfer to " + str(accountTo.getId()) + ", value: " + str(amount),
            #                  accountFrom.getId())
            # h_to = History("Incoming transfer from " + str(accountFrom.getId()) + ", value: " + str(amount),
            #                accountTo.getId())
            # accountFrom.getHistory().append(h_from)
            # accountTo.getHistory().append(h_to)
            return True
