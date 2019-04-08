import importlib
from db_factory import DBFactory


class DB(DBFactory):
    def __init__(self):
        self.db_engine = open("conf/db.conf").readline().strip()

    def get_db_factory(self):
        module_name = "factory.%s_factory" % self.db_engine.lower()
        factory_class_name = "%sFactory" % self.db_engine
        factory_module = importlib.import_module(module_name)
        factory_class = getattr(factory_module, factory_class_name)
        return factory_class()

    def get_user_session(self):
        return self.get_db_factory().get_user_session()

    def get_department_session(self):
        return self.get_db_factory().get_department_session()
