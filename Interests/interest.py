from abc import ABCMeta, abstractmethod


class Interest:
    __metaclass__ = ABCMeta

    def __init__(self, value, percent):
        Interest.__init__(self, value, percent)


    @abstractmethod
    def get_interests_value(self, money): raise NotImplemented