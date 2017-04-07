from abc import ABCMeta, abstractmethod


class Interest:
    __metaclass__ = ABCMeta

    def __init__(self, percent):
        self.percent = percent

    @abstractmethod
    def get_interests_value(self, money): raise NotImplemented