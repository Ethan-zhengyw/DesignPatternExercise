from abc import abstractmethod, ABCMeta

MODE_SIMPLIFY = "SIMPLIFY"
MODE_MEMORY = "MEMORY"
MODE_FULL = "FULL"
MODE = (MODE_SIMPLIFY, MODE_MEMORY, MODE_FULL, )


class Screen:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def show(self):
        for comp in self.components:
            print "Displaying components: %s" % comp


class ScreenBuilder:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.screen = Screen()

    @abstractmethod
    def build_menu(self):
        pass

    @abstractmethod
    def build_main_window(self):
        pass

    @abstractmethod
    def build_control_bar(self):
        pass

    @abstractmethod
    def build_play_list(self):
        pass

    @abstractmethod
    def build_collection_list(self):
        pass

    def get_screen(self):
        return self.screen


class SimplifyModeBuilder(ScreenBuilder):
    def build_menu(self):
        print "Not Displaying: Menu(Simplify Mode)."

    def build_main_window(self):
        print "Displaying: Main Window(Simplify Mode)."

    def build_control_bar(self):
        print "Displaying: Control Bar(Simplify Mode)."

    def build_play_list(self):
        print "Not Displaying: Play List(Simplify Mode)."

    def build_collection_list(self):
        print "Not Displaying: Collection List(Simplify Mode)."


class MemoryModeBuilder(ScreenBuilder):
    def build_menu(self):
        print "Not Displaying: Menu(Memory Mode)."

    def build_main_window(self):
        print "Displaying: Main Window(Memory Mode)."

    def build_control_bar(self):
        print "Displaying: Control Bar(Memory Mode)."

    def build_play_list(self):
        print "Not Displaying: Play List(Memory Mode)."

    def build_collection_list(self):
        print "Displaying: Collection List(Memory Mode)."


class FullModeBuilder(ScreenBuilder):
    def build_menu(self):
        print "Displaying: Menu(Full Mode)."

    def build_main_window(self):
        print "Displaying: Main Window(Full Mode)."

    def build_control_bar(self):
        print "Displaying: Control Bar(Full Mode)."

    def build_play_list(self):
        print "Displaying: Play List(Full Mode)."

    def build_collection_list(self):
        print "Not Displaying: Collection List(Full Mode)."


class ScreenDirector:
    # combine with simple factory pattern
    def __init__(self):
        pass

    @staticmethod
    def construct(screen_builder):
        screen_builder.build_main_window()
        screen_builder.build_control_bar()
        screen_builder.build_menu()
        screen_builder.build_play_list()
        screen_builder.build_collection_list()
