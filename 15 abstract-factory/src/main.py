from model.base.user import User
from model.base.department import Department
from factory.db_factory import DBFactory
from factory.mysql_factory import MySQLFactory
from factory.mongodb_factory import MongoDBFactory


def main():
    # get user/department session by a MySQL DB Factory
    db_factory = MySQLFactory()
    user_session = db_factory.get_user_session()
    department_session = db_factory.get_department_session()
    user_session.add()
    user_session.get()
    department_session.add()
    department_session.get()

    # get user/department session by a MongoDB DB Factory
    # only need to change MySQLFactory to MongoDBFactory
    db_factory = MongoDBFactory()
    user_session = db_factory.get_user_session()
    department_session = db_factory.get_department_session()
    user_session.add()
    user_session.get()
    department_session.add()
    department_session.get()


main()
