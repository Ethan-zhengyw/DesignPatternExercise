from abc import ABCMeta, abstractmethod
import const


class DoorState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def handle_event(self, dcs, e):
        pass


class DoorStateOpening(DoorState):

    def handle_event(self, dcs, e):
        if e not in (const.EVENT_DOOR_COMPLETE_OPENED,):
            print "Warning: current state is DoorStateOpening, only EVENT_DOOR_COMPLETE_OPENED is valid, ignoring..."
        else:
            dcs.stop()


class DoorStateClosed(DoorState):

    def handle_event(self, dcs, e):
        if e not in (const.EVENT_BUTTON_PRESSED,):
            print "Warning: current state is DoorStateClosed, only EVENT_BUTTON_PRESSED is valid, ignoring..."
        else:
            dcs.open()


class DoorStateOpen(DoorState):

    def handle_event(self, dcs, e):
        if e not in (const.EVENT_LIGHT_BARRIER_INTERRUPTED,
                     const.EVENT_TIMEOUT):
            print "Warning: current state is DoorStateOpen, " \
                  "only EVENT_LIGHT_BARRIER_INTERRUPTED and EVENT_TIMEOUT is valid, ignoring..."
        elif const.EVENT_LIGHT_BARRIER_INTERRUPTED == e:
            dcs.start()
        elif const.EVENT_TIMEOUT == e:
            dcs.close()


class DoorStateClosing(DoorState):

    def handle_event(self, dcs, e):
        if e not in (const.EVENT_BUTTON_PRESSED,
                     const.EVENT_LIGHT_BARRIER_INTERRUPTED,
                     const.EVENT_DOOR_COMPLETE_CLOSED):
            print "Warning: current state is DoorStateOpening, " \
                  "only EVENT_BUTTON_PRESSED, EVENT_LIGHT_BARRIER_INTERRUPTED, " \
                  "and EVENT_DOOR_COMPLETE_CLOSED is valid, ignoring..."
        elif e in (const.EVENT_BUTTON_PRESSED, const.EVENT_LIGHT_BARRIER_INTERRUPTED,):
            dcs.open()
        elif const.EVENT_DOOR_COMPLETE_CLOSED == e:
            dcs.stop()

