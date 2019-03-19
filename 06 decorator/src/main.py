import clothes_decorator as cd


def main():
    print "Become free style: "
    tom = cd.Person()
    free_style_tom = cd.TrouserDecorator(cd.TShirtsDecorator(cd.SlippersDecorator(tom)))
    free_style_tom.show()

    print "Become formal style: "
    tom = cd.Person()
    formal_style_tom = cd.SuitDecorator(cd.TieDecorator(cd.LeatherShoesDecorator(tom)))
    formal_style_tom.show()


main()

