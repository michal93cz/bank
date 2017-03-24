from abc import ABCMeta, abstractmethod


class Interest:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_interests_value(self, money): raise NotImplemented

