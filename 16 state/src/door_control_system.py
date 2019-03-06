import time
from threading import Thread

import const
import door_state


class TimerThread(Thread):
    def __init__(self, dcs, count):
        Thread.__init__(self)
        self.dcs = dcs
        self.count = count

    def reset_count(self, new_count):
        print "Info: Timer, reset to %s." % new_count
        self.count = new_count

    def run(self):
        while self.count > 0:
            print "Info: Timer, counting, %s..." % self.count
            time.sleep(1)
            self.count -= 1
        print "Info: Timer, time out!"
        self.dcs.door_state.handle_event(self.dcs, const.EVENT_TIMEOUT)


class DoorControlSystem:

    def __init__(self,
                 state=door_state.DoorStateClosed(),
                 timer_count=10):
        self.door_state = state
        self.timer_count = timer_count
        self.timer_thread = TimerThread(self, timer_count)
        print "Info: DoorControlSystem initialized, current state is DoorStateClosed."

    def open(self):
        print "Info: current state is %s, now open the door, " \
              "state enter DoorStateOpening..." % self.door_state.__class__.__name__
        self.door_state = door_state.DoorStateOpening()

    def close(self):
        print "Info: current state is %s, now close the door, " \
              "state enter DoorStateClosing..." % self.door_state.__class__.__name__
        self.door_state = door_state.DoorStateClosing()

    def start(self):
        if self.timer_thread.isAlive():
            self.timer_thread.reset_count(self.timer_count)
        else:
            self.timer_thread = TimerThread(self, self.timer_count)
            self.timer_thread.start()

    def stop(self):
        if isinstance(self.door_state, door_state.DoorStateOpening):
            print "Info: current state is DoorStateOpening, now stop the door, " \
                  "state enter DoorStateOpen."
            self.door_state = door_state.DoorStateOpen()
            self.start()
        elif isinstance(self.door_state, door_state.DoorStateClosing):
            print "Info: current state is DoorStateClosing, now stop the door, " \
                  "state enter DoorStateClosed."
            self.door_state = door_state.DoorStateClosed()

    def go(self):
        while True:
            print "Current state is %s, please input event to trigger door state transformation.\n" \
                "1 - EVENT_BUTTON_PRESSED\n" \
                "2 - EVENT_DOOR_COMPLETE_OPENED\n" \
                "3 - EVENT_DOOR_COMPLETE_CLOSED\n" \
                "4 - EVENT_LIGHT_BARRIER_INTERRUPTED" % self.door_state.__class__.__name__
            event = raw_input()
            if "1" == event:
                self.door_state.handle_event(self, const.EVENT_BUTTON_PRESSED)
            elif "2" == event:
                self.door_state.handle_event(self, const.EVENT_DOOR_COMPLETE_OPENED)
            elif "3" == event:
                self.door_state.handle_event(self, const.EVENT_DOOR_COMPLETE_CLOSED)
            elif "4" == event:
                self.door_state.handle_event(self, const.EVENT_LIGHT_BARRIER_INTERRUPTED)
            else:
                print "Warning: unexpected input, ignoring..."
