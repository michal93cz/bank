from abc import ABCMeta, abstractmethod

# interfejs dla konta bankowych - Component ze wzoraca Decorator
class BankAccountComponent:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_bank_id(self): raise NotImplemented

    @abstractmethod
    def get_account_balance(self): raise NotImplemented

    @abstractmethod
    def subtract(self, money: int): raise NotImplemented

    @abstractmethod
    def add(self, money: int): raise NotImplemented
