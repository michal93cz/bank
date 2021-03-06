from Interests.interest import Interest


class AccountInterestA(Interest):
    def get_interests_value(self, product):
        money = product.getBalance()

        if money < 1000:
            percent = 0.02
        elif money < 3000:
            percent = 0.05
        else:
            percent = 0.1
        return money * percent
