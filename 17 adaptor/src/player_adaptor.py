from abc import ABCMeta, abstractmethod


class Player:
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass


class Forward(Player):
    def attack(self):
        print "Forward [%s] attack" % self.name

    def defense(self):
        print "Forward [%s] defense" % self.name


class Center(Player):
    def attack(self):
        print "Center [%s] attack" % self.name

    def defense(self):
        print "Center [%s] defense" % self.name


class Guard(Player):
    def attack(self):
        print "Guard [%s] attack" % self.name

    def defense(self):
        print "Guard [%s] defense" % self.name


# Adaptee
class ForeignPlayer:
    def __init__(self, name):
        self.name = name

    def foreign_attack(self):
        print "ForeignPlayer [%s] foreign attack" % self.name

    def foreign_defense(self):
        print "ForeignPlayer [%s] foreign defense" % self.name


# Adaptor
class Translator(Player):
    def __init__(self, name):
        super(Translator, self).__init__(name)
        self.foreign_player = ForeignPlayer(name)

    def attack(self):
        self.foreign_player.foreign_attack()

    def defense(self):
        self.foreign_player.foreign_defense()
