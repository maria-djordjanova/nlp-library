class Document:
    def __init__(self, author=None, title=None, pubDate=None, text=None):
        if isinstance(author, str):
            self._author = author
        else:
            Exception('author should be string')

        if isinstance(title, str):
            self._title = title
        else:
            Exception('title should be string')

        if isinstance(pubDate, str):
            self._pubDate = pubDate
        else:
            Exception('date should be string')

        if isinstance(text, str):
            self._text = text
        else:
            Exception('text should be string')

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def pubDate(self):
        return self._pubDate

    @property
    def text(self):
        return self._text
