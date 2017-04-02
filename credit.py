from bank_product import BankProduct
import time
from Interests.credit_interest import CreditInterest


class Credit(BankProduct):
    def __init__(self, money, account, end_date, user_id, product_id, number_of_installment):
        BankProduct.__init__(self, user_id=user_id, product_id=product_id, type='credit')
        self._money = money
        self._account = account
        self._begin_date = time.asctime(time.localtime(time.time()))
        self._end_date = end_date
        self._number_of_installment = number_of_installment
        self._installment_to_pay = number_of_installment
        self._interest = CreditInterest(value=money, percent=5)
        account.deposit(money)

    def pay_one_installment(self):
        print("One installment pay, value: " + str(self._interest.get_interests_value(self._money/self._number_of_installment) + self._money/self._number_of_installment))
        self._installment_to_pay -= 1
        self._account.pay_interest(self._interest.get_interests_value(self._money/self._number_of_installment) + self._money/self._number_of_installment)

    def close_product(self, interests):
        to_pay = self._money+(self._money*interests)
        payed = self._account.withdraw(to_pay)
        if (payed is not None) and (payed == to_pay):
            print("Kredyt spłacony")
            return True
        else:
            print("Brak wystarczających środków do spłaty kredytu")
            return False

    def get_credit_value(self):
        return self._money

    def get_account(self):
        return self._account

    def get_begin_date(self):
        return self._begin_date

    def get_end_date(self):
        return self._end_date
