from model.base.department import Department


class MongoDBDepartment(Department):
    @staticmethod
    def add():
        print "Add MongoDBDepartment."

    @staticmethod
    def get():
        print "Get MongoDBDepartment"
