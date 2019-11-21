from nlplib.core.document import Document
from nlplib.utils.logger import Logger


class Parser:
    def __init__(self):
        self.logger = Logger()
        pass

    def parse_file(self, filename):
        self.logger.log.debug('parse file')

        with open(filename) as file:
            author = file.readline()
            title = file.readline()
            pubDate = file.readline()

            text = file.readline()
            while text:
                text = text + file.readline()

            return Document(author, title, pubDate, text)

    def parse_document(self, document):
        self.logger.log.debug('parse document')

    def parse_text(self, text):
        self.logger.log.debug('parse text')

    def parse_sentence(self, sentence):
        self.logger.log.debug('parse sentence')

    def parse_word(self, word):
        self.logger.log.debug('parse word')
