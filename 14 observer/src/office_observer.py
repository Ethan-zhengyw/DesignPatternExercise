from abc import ABCMeta, abstractmethod


STAFF_STATE_WORKING = "WORKING"
STAFF_STATE_WATCHING_NBA = "WATCHING_NBA"
STAFF_STATE_WATCHING_STOCK = "WATCHING_STOCK"
STAFF_STATE = (STAFF_STATE_WORKING, STAFF_STATE_WATCHING_NBA, STAFF_STATE_WATCHING_STOCK,)

MSG_BOSS_I_COMING = "MSG_BOSS_I_COMING"
MSG_BOSS_I_LEFT = "MSG_BOSS_I_LEFT"
MSG_SEC_BOSS_COMING = "MSG_SEC_BOSS_COMING"
MSG_SEC_BOSS_LEFT = "MSG_SEC_BOSS_LEFT"


class Subject:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.observers = []
        self.state = None

    def attach(self, o):
        self.observers.append(o)

    def detach(self, o):
        self.observers.remove(o)

    def notify(self):
        for o in self.observers:
            o.update()

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state


class Observer:
    __metaclass__ = ABCMeta

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.state = STAFF_STATE_WORKING

    def set_subject(self, subject):
        self.subject = subject

    @abstractmethod
    def update(self):
        pass


class NBAObserver(Observer):
    def update(self):
        msg = self.subject.get_state()
        print "I'm %s fans." % self.name
        print "Current state is: %s." % self.state
        print "Event message is: %s." % msg

        if msg == MSG_BOSS_I_LEFT:
            self.state = STAFF_STATE_WATCHING_NBA
        if msg == MSG_SEC_BOSS_COMING:
            self.state = STAFF_STATE_WORKING

        print "State change to %s.\n" % self.state


class StockObserver(Observer):
    def update(self):
        msg = self.subject.get_state()
        print "I'm %s fans." % self.name
        print "Current state is: %s." % self.state
        print "Event message is: %s." % msg

        if msg == MSG_BOSS_I_LEFT:
            self.state = STAFF_STATE_WATCHING_STOCK
        if msg == MSG_SEC_BOSS_COMING:
            self.state = STAFF_STATE_WORKING

        print "State change to %s.\n" % self.state


class Boss(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.state = MSG_BOSS_I_LEFT


class Secretary(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.state = MSG_SEC_BOSS_COMING
