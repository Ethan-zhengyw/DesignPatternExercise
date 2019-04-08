from abc import abstractmethod, ABCMeta


class User:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get(self):
        pass
