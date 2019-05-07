import time
import thread
from singleton import Singleton
from multiprocessing import Process, Pipe


instances = set()


def test_pipe(pipe, i):
    s = Singleton.get_instance()
    pipe.send(s)
    print "This is process", i, s


def test():
    s = Singleton.get_instance()
    print s
    instances.add(s)


def main():
    s = Singleton()
    print s

    s = Singleton.get_instance()
    print s

    s = Singleton.get_instance()
    print s


def main_thread():
    for i in range(100):
        thread.start_new_thread(test, ())


def main_process_pipe():
    parent_conn, child_conn = Pipe()
    ps = []
    for i in range(100):
        p = Process(target=test_pipe, args=(child_conn, i))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    instances.add(parent_conn.recv())
    print "set %d: %s" % (len(instances), instances)


main()
main_thread()
# main_process_pipe()
