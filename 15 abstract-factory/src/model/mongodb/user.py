from model.base.user import User


class MongoDBUser(User):
    @staticmethod
    def add():
        print "Add MongoDBUser."

    @staticmethod
    def get():
        print "Get MongoDBUser"
