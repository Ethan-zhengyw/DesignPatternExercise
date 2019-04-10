class ArticleMemento:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class Article:
    def __init__(self, content):
        print "Initialize article with content: %s" % content
        self.content = content

    def set_content(self, content):
        print "Set article with content: %s" % content
        self.content = content

    def create_memento(self):
        print "Create article memento with content: %s" % self.content
        return ArticleMemento(self.content)

    def restore(self, article_memento):
        print "Restore article memento with content: %s" % article_memento.get_content()
        self.content = article_memento.get_content()


class ArticleMementoCaretaker:
    def __init__(self):
        self.article_mementos = []

    def get_size(self):
        return len(self.article_mementos)

    def add_article_memento(self, article_memento):
        print "ArticleMementoCaretaker add memento with content: %s"\
              % article_memento.get_content()
        self.article_mementos.append(article_memento)

    def get_article_memento(self, index):
        print "ArticleMementoCaretaker return memento with content: %s" \
              % self.article_mementos[index].get_content()
        return self.article_mementos[index]
