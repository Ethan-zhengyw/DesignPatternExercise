from abc import ABCMeta, abstractmethod


class Iterator:
    __metaclass__ = ABCMeta

    def __init__(self, aggregates):
        self.aggregates = aggregates
        self.current = 0

    @abstractmethod
    def first_item(self):
        pass

    @abstractmethod
    def next_item(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def current_item(self):
        pass


class Aggregate:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def create_iterator(self):
        pass


class BooksAggregate(Aggregate):
    def __init__(self):
        super(BooksAggregate, self).__init__()
        self.titles = ["A", "B", "C", "D"]

    def create_iterator(self):
        return BookIterator(self)

    def get(self, index):
        return self.titles[index]

    def get_size(self):
        return len(self.titles)


class BookIterator(Iterator):
    def __init__(self, books):
        super(BookIterator, self).__init__(self)
        self.books = books
        self.current = 0

    def first_item(self):
        if len(self.books) > 0:
            return self.books.get(0)
        else:
            return None

    def next_item(self):
        if self.current < self.books.get_size() - 1:
            self.current += 1
            return self.books.get(self.current)
        else:
            return None

    def current_item(self):
        return self.books.get(self.current)

    def is_done(self):
        return self.current == self.books.get_size() - 1
