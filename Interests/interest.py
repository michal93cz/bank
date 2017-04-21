from abc import ABCMeta, abstractmethod
import bank_product


class Interest:
    __metaclass__ = ABCMeta

    def __init__(self, b):
        self.product = b

    @abstractmethod
    def get_interests_value(self): raise NotImplemented
