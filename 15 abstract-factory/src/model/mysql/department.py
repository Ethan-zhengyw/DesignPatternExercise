from model.base.department import Department


class MySQLDepartment(Department):
    @staticmethod
    def add():
        print "Add MySQLDepartment."

    @staticmethod
    def get():
        print "Get MySQLDepartment"
