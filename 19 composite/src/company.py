from abc import  ABCMeta, abstractmethod


class Company:
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_structure(self, depth):
        pass

    @abstractmethod
    def do_duty(self):
        pass


class HRDepartment(Company):
    def display_structure(self, depth):
        print "-" * depth + self.name

    def do_duty(self):
        print "[%s] do duty." % self.name


class FinanceDepartment(Company):
    def display_structure(self, depth):
        print "-" * depth + self.name

    def do_duty(self):
        print "[%s] do duty." % self.name


class ConcreteCompany(Company):
    def __init__(self, name):
        super(ConcreteCompany, self).__init__(name)
        self.departments = []

    def display_structure(self, depth):
        print "-" * depth + "[%s]" % self.name

        for dept in self.departments:
            dept.display_structure(depth + 2)

    def do_duty(self):
        print "[%s] 's departments do duty:" % self.name

        for dept in self.departments:
            dept.do_duty()

    def add_department(self, company):
        self.departments.append(company)

    def remove_department(self, company):
        self.departments.remove(company)
