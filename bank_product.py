from Interests.account_interest_a import AccountInterestA
from Interests.interest import Interest
from bank_element import BankElement


class BankProduct(BankElement):
    def __init__(self, bank_id: int, user_id: int, product_id: int, type):
        self._user_id = user_id
        self._product_id = product_id
        self._type = type
        self._bank_id = bank_id
        self._history = []
        self._interest = AccountInterestA()

    def closeProduct(self):
        pass

    def getOwner(self):
        return self._user_id

    def getId(self):
        return self._product_id

    def getType(self):
        return self._type

    def getHistory(self):
        return self._history

    def getBalance(self):
        pass

    def setInterest(self, interest: Interest):
        self._interest = interest

    def getInterests(self):
        self._interest.get_interests_value(self)

    def accept(self, visitor):
        pass
