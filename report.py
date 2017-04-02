from bank_account import BankAccount


class Report:
    @staticmethod
    def sum_of_founds_in_bank(products):
        founds_sum = 0
        for product in products:
            if type(product) is BankAccount:
                founds_sum += product.current_account_balance()
        return founds_sum

    def sum_of_transactions(self, history, begin_date, end_date):
        pass

    @staticmethod
    def sum_of_debits(products):
        debits_sum = 0
        for product in products:
            if type(product) is BankAccount:
                if product.current_account_balance() < 0:
                    debits_sum += -product.current_account_balance()
        return debits_sum
