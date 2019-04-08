from model.base.user import User


class MySQLUser(User):
    @staticmethod
    def add():
        print "Add MySQLDBUser."

    @staticmethod
    def get():
        print "Get MySQLDBUser"
