def singleton_dec(cls):
    print "cls: ", cls
    _instance = {}

    def _singleton(*args, **kargs):
        print "args: ", args
        print "kargs: ", kargs
        print "_instance: ", _instance
        if cls not in _instance:
            print "cls not in _instance"
            _instance[cls] = cls(*args, **kargs)
        else:
            print "cls in _instance"
        return _instance[cls]

    return _singleton


print "singleton line 15"


@singleton_dec
class Singleton(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


print "Singleton: ", Singleton


