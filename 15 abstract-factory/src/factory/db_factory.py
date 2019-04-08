from abc import ABCMeta, abstractmethod
import model.base.user
import model.base.department


class DBFactory:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def get_user_session():
        pass

    @staticmethod
    @abstractmethod
    def get_department_session():
        pass
