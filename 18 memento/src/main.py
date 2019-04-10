from article_memento import Article, ArticleMemento, ArticleMementoCaretaker


def main():
    content1 = "I have book a book."
    content2 = "I have book a book at the book store."
    content3 = "I canceled booking a book at the book store."

    backups = ArticleMementoCaretaker()

    article = Article(content1)
    backups.add_article_memento(article.create_memento())

    article.set_content(content2)
    backups.add_article_memento(article.create_memento())

    article.set_content(content3)
    backups.add_article_memento(article.create_memento())

    size = backups.get_size()

    # perform undo action
    print "\nUndoing..."
    for i in range(size - 2, -1, -1):
        article.restore(backups.get_article_memento(i))

    # perform redo action
    print "\nRedoing..."
    for i in range(1, size):
        article.restore(backups.get_article_memento(i))


main()
