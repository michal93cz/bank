from abc import ABCMeta, abstractmethod
from bank_product import BankProduct

class Interest:
    __metaclass__ = ABCMeta

    def __init__(self, b: BankProduct):
        self.product = b

    @abstractmethod
    def get_interests_value(self): raise NotImplemented
