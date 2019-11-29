import unittest

from nlplib.utils.logger import Logger
from nlplib.utils.parser import Parser


class TestParser(unittest.TestCase):

    def __init__(self, name=None):
        super(TestParser, self).__init__()
        self.logger = Logger(name)

    def parse_file(self, filename, author, title, pubDate):
        self.logger.log.debug('TEST: parse file: ' + filename)

        document = Parser().parse_file(filename)

        self.assertEqual(document.author, author)
        self.assertEqual(document.title, title)
        self.assertEqual(document.pubDate, pubDate)


if __name__ == "__main__":
    parser = TestParser()

    parser.parse_file('../assets/data/sample1.txt',
                      'John Ronald Reuel Tolkien',
                      'The Lord Of The Rings: The Fellowship of the Ring',
                      '1954')

    parser.parse_file('../assets/data/sample2.txt',
                      'John Ronald Reuel Tolkien',
                      'The Hobbit: Or There and Back Again',
                      '1937')

    parser.parse_file('../assets/data/sample3.txt',
                      'Franz Kafka',
                      'Metamorphosis',
                      '1915')
