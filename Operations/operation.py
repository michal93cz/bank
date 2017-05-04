from abc import abstractmethod


class Operation:
    @abstractmethod
    def execute(self):
        pass
