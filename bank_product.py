from Interests.account_interest_a import AccountInterestA
from Interests.interest import Interest

class BankProduct:

    def __init__(self, user_id, product_id, type):
        self._user_id = user_id
        self._product_id = product_id
        self._type = type
        self._history = []
        self._interest = AccountInterestA(self)

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