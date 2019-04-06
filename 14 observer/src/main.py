from office_observer import NBAObserver, StockObserver, Boss, Secretary


def main():
    # NBA fans watching NBA after boss leave
    # Stock fans watching stock after boss leave
    boss = Boss()
    observer_nba = NBAObserver("NBA", boss)
    observer_stock = StockObserver("STOCK", boss)
    boss.attach(observer_nba)
    boss.attach(observer_stock)
    boss.notify()

    # Every one back to work once secretary notify that boss coming!
    secretary = Secretary()
    observer_nba.set_subject(secretary)
    observer_stock.set_subject(secretary)
    secretary.attach(observer_nba)
    secretary.attach(observer_stock)
    secretary.notify()


main()
