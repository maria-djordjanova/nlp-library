class Sentence:
    def __init__(self, sentence=None):
        if isinstance(sentence, str):
            self.words = sentence.split(' ')
        else:
            Exception('sentence should be string')

    @property
    def words(self):
        return self._words
