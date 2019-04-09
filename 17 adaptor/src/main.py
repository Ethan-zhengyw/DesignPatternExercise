from player_adaptor import Forward, Center, Guard, Translator


def main():
    forward = Forward("A")
    center = Center("B")
    guard = Guard("C")
    foreign_player = Translator("D")

    players = [forward, center, guard, foreign_player]
    for player in players:
        player.attack()
        player.defense()


main()
