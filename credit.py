import time
from Interests.credit_interest import CreditInterest
from history import History
from bank_product import BankProduct


class Credit(BankProduct):
    def __init__(self, money, account, end_date, user_id, product_id, number_of_installment, bank_id):
        BankProduct.__init__(self, bank_id=bank_id, user_id=user_id, product_id=product_id, type='credit')
        self._money = money
        self._account = account
        self._begin_date = time.asctime(time.localtime(time.time()))
        self._end_date = end_date
        self._number_of_installment = number_of_installment
        self._installment_to_pay = number_of_installment
        self._interest = CreditInterest()
        account.deposit(money)
        self._history.append(History("Credit started with value: " + str(money), self.getId()))

    def pay_one_installment(self):
        if self._installment_to_pay < 0:
            raise ValueError("Wszystkie raty zostały spłacone")
        value_str = str(self._interest.get_interests_value(
            self._money / self._number_of_installment) + self._money / self._number_of_installment)
        print("One installment pay, value: " + value_str)
        self._history.append(History("One installment pay, value: " + value_str, self.getId()))
        self._installment_to_pay -= 1
        self._account.pay_interest(self._interest.get_interests_value(
            self._money / self._number_of_installment) + self._money / self._number_of_installment)

    def close_product(self):
        to_pay = self._money + (self._interest.get_interests_value(self._money))
        payed = self._account.withdraw(to_pay)
        if (payed is not None) and (payed == to_pay):
            self._installment_to_pay = 0
            print("Credit payed.")
            self._history.append(History("Credit payed and closed.", self.getId()))
            return True
        else:
            print("Not enough money to pay credit.")
            return False

    def get_credit_value(self):
        return self._money

    def get_account(self):
        return self._account

    def get_begin_date(self):
        return self._begin_date

    def get_end_date(self):
        return self._end_date

    def getBalance(self):
        return self._money

    def accept(self, visitor):
        return visitor.visit_credit(self)
