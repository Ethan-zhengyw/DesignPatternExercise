from abc import ABCMeta, abstractmethod

class Person:
    def __init__(self):
        pass

    def show(self):
        print "Nake yet"


class ClothesDecorator:
    __metaclass__ = ABCMeta

    def __init__(self, person):
        # decorate while initialize
        # can be done by implementing a decorating method as well
        self.person = person

    @abstractmethod
    def show(self):
        pass


class SlippersDecorator(ClothesDecorator):
    def show(self):
        self.person.show()
        print "Slippers"


class TShirtsDecorator(ClothesDecorator):
    def show(self):
        self.person.show()
        print "TShirts"


class TrouserDecorator(ClothesDecorator):
    def show(self):
        self.person.show()
        print "Trouser"


class TieDecorator(ClothesDecorator):
    def show(self):
        self.person.show()
        print "Tie"


class LeatherShoesDecorator(ClothesDecorator):
    def show(self):
        self.person.show()
        print "LeatherShoes"


class SuitDecorator(ClothesDecorator):
    def show(self):
        self.person.show()
        print "Suit"

