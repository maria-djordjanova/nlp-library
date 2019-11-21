import logging

from nlplib.utils.colored_formatter import ColoredFormatter


RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


class Logger:
    FORMAT = "[$BOLD%(name)-10s$RESET][%(levelname)-10s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)

    def __init__(self, name=None):
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.DEBUG)

        formatter = ColoredFormatter(self.COLOR_FORMAT)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.log.addHandler(ch)
