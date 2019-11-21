import logging


class Logger:
    def __init__(self, name=None):
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.log.addHandler(ch)
