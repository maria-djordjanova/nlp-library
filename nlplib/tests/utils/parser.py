from nlplib.utils.logger import Logger


class TestParser:

    def __init__(self, name=None):
        self.logger = Logger(name)

    def test_parse_file(self):
        self.logger.log.debug('testing parse file')


if __name__ == "__main__":
    parser = TestParser()
    parser.test_parse_file()
