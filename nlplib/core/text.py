class Text:
    def __init__(self, text=None):
        if isinstance(text, str):
            self._sentences = text.split('.')
        else:
            Exception('text should be string')

    @property
    def sentences(self):
        return self._sentences
