from abc import abstractmethod, ABCMeta


class Department:
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get(self):
        pass
