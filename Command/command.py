from abc import ABCMeta, abstractmethod


class Command:
    @abstractmethod
    def execute(self):
        pass
