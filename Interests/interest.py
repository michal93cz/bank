from abc import ABCMeta, abstractmethod
from bank_product import BankProduct


class Interest:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_interests_value(self, product: BankProduct): raise NotImplemented
