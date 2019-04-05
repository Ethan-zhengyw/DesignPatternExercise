import screen_builder as sb


def main():
    # Simplify Mode
    print "----Constructing Simplify Mode Screen----"
    screen_director = sb.ScreenDirector()
    mode_builder = sb.SimplifyModeBuilder()
    screen_director.construct(mode_builder)
    screen = mode_builder.get_screen()
    screen.show()
    print "----End Constructing Simplify Mode Screen----\n"

    # Memory Mode
    print "----Constructing Memory Mode Screen----"
    mode_builder = sb.MemoryModeBuilder()
    screen_director.construct(mode_builder)
    screen = mode_builder.get_screen()
    screen.show()
    print "----End Constructing Memory Mode Screen----\n"

    # Full Mode
    print "----Constructing Full Mode Screen----"
    mode_builder = sb.FullModeBuilder()
    screen_director.construct(mode_builder)
    screen = mode_builder.get_screen()
    screen.show()
    print "----End Constructing Full Mode Screen----\n"


main()
