from nlplib.utils.logger import Logger
from nlplib.utils.parser import Parser


class TestParser:

    def __init__(self, name=None):
        self.logger = Logger(name)

    def test_parse_file(self, filename):
        self.logger.log.debug('testing parse file')

        document = Parser().parse_file(filename)
        print(document.author)


if __name__ == "__main__":
    parser = Parser()
    parser.parse_file('../assets/data/sample1.txt')

