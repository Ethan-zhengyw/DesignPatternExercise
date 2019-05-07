class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            # call by user during program running
            raise Exception("Can't initialize singleton class!")
        else:
            # call by static method
            Singleton._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            Singleton()
        return cls._instance
