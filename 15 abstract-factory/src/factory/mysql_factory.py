from db_factory import DBFactory
from model.mysql.user import MySQLUser
from model.mysql.department import MySQLDepartment


class MySQLFactory(DBFactory):
    @staticmethod
    def get_user_session():
        return MySQLUser()

    @staticmethod
    def get_department_session():
        return MySQLDepartment()
