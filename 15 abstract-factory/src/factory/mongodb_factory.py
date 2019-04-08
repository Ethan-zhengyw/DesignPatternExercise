from db_factory import DBFactory
from model.mongodb.user import MongoDBUser
from model.mongodb.department import MongoDBDepartment


class MongoDBFactory(DBFactory):
    @staticmethod
    def get_user_session():
        return MongoDBUser()

    @staticmethod
    def get_department_session():
        return MongoDBDepartment()
