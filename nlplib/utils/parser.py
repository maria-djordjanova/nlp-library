import logging

from nlplib.core.document import Document


class Parser:
    logging.config.fileConfig('../../config/logger.yaml', False)

    @staticmethod
    def parseFile(filename):
        logging.info('parsing file')

        with open(filename) as file:
            author = file.readline()
            title = file.readline()
            pubDate = file.readline()

            text = file.readline()
            while text:
                text = text + file.readline()

            return Document(author, title, pubDate, text)

    @staticmethod
    def parseDocument(document):
        logging.info('parsing document')

    @staticmethod
    def parseText(text):
        logging.info('parsing text')

    @staticmethod
    def parseSentence(sentence):
        logging.info('parsing sentence')

    @staticmethod
    def parseWord(word):
        logging.info('parsing word')
