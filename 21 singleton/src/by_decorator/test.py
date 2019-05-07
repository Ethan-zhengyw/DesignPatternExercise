from singleton import Singleton


def main():
    print "test line 5"
    a1 = Singleton(2)
    print "test line 7"
    a2 = Singleton(3)
    print "test line 9"
    print a1, a1.x, a1.a
    print a2, a1.x, a1.a


if __name__ == "__main__":
    main()
