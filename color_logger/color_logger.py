import sys
from enum import Enum
import logging


use_color = True

class Colors(Enum):
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'


_LOG_COLORS = {
    'WARNING': Colors.YELLOW,
    'INFO': Colors.BLUE,
    'DEBUG': Colors.CYAN,
    'CRITICAL': Colors.RED,
    'ERROR': Colors.RED
}


class ColorFormatter(logging.Formatter):
    def __init__(self, msg: str) -> None:
        super(ColorFormatter, self).__init__(msg)

    def format(self, record: logging.LogRecord) -> str:
        levelname = record.levelname
        if use_color:
            record.color = _LOG_COLORS[levelname].value  # type: ignore
            record.reset = Colors.RESET.value  # type: ignore
        else:
            record.color, record.reset = "", ""  # type: ignore
        return logging.Formatter.format(self, record)


class ColorLogger(logging.Logger):
    FORMAT = ("%(color)s%(levelname)8s %(name)30s.py%(funcName)"
              "20s:L%(lineno)d: %(message)s %(reset)s")
    # FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"

    def __init__(self, name: str) -> None:
        logging.Logger.__init__(self, name, logging.DEBUG)
        color_formatter = ColorFormatter(self.FORMAT)
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(color_formatter)
        self.addHandler(console)


def cprint(string: str, color: Colors) -> None:
    if use_color:
        print(color.value + string + Colors.RESET.value)
    else:
        print(string)
