class Word:
    def __init__(self, word=None):
        if isinstance(word, str):
            self._word = word
        else:
            Exception('word should be string')

    @property
    def word(self):
        return self._word
