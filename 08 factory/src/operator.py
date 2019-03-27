from abc import ABCMeta, abstractmethod


class Operator:

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_result(self, number_a, number_b):
        pass


class OperatorAdd(Operator):
    def get_result(self, number_a, number_b):
        return number_a + number_b


class OperatorSub(Operator):
    def get_result(self, number_a, number_b):
        return number_a - number_b


class OperatorMul(Operator):
    def get_result(self, number_a, number_b):
        return number_a * number_b


class OperatorDiv(Operator):
    def get_result(self, number_a, number_b):
        if number_b == 0:
            return Exception("Divisor can not be zero!")
        else:
            return number_a / number_b
