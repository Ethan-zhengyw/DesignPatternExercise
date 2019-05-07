import threading
from singleton import Singleton


def task(name):
    print Singleton(name)


if __name__ == "__main__":
    for i in range(10):
        t = threading.Thread(target=task, args=("name",))
        t.start()
