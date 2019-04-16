from book_iterator import BookIterator, BooksAggregate


def main():
    books = BooksAggregate()
    books_iter = books.create_iterator()

    print "Current book: %s" % books_iter.current_item()
    while books_iter.next_item():
        print "Current book: %s" % books_iter.current_item()


main()
