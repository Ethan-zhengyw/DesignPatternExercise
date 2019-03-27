from abc import ABCMeta, abstractmethod
import operator as op


class OperatorFactory:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def create_operator(self):
        pass


class AddFactory(OperatorFactory):
    def create_operator(self):
        return op.OperatorAdd()


class SubFactory(OperatorFactory):
    def create_operator(self):
        return op.OperatorSub()


class MulFactory(OperatorFactory):
    def create_operator(self):
        return op.OperatorMul()


class DivFactory(OperatorFactory):
    def create_operator(self):
        return op.OperatorDiv()
