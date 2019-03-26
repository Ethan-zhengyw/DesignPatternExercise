from abc import ABCMeta, abstractmethod
import uuid
import time


class Handler:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def read(self, key):
        pass


class FileHandler(Handler):
    def __init__(self, file_content):
        self.file_content = file_content

    def read(self, key):
        # pretend to read key from a big file
        time.sleep(1)
        return self.file_content.get(key) if key in self.file_content else uuid.uuid4()


class FileProxy(Handler):
    def __init__(self, file_content):
        self.cache_content = dict()
        self.file_handler = FileHandler(file_content)

    def read(self, key):
        if key in self.cache_content:
            print "Cache hit! return from cache content: %s=%s."\
                  % (key, self.cache_content.get(key))
        else:
            result = self.file_handler.read(key)
            print "Cache Missing! read from file content: %s=%s, " \
                  "now key %s is cached." % (key, result, key)
            self.cache_content[key] = result
