import logging
import color_logger
from color_logger import cprint, Colors

def test_all_functions():
    logging.setLoggerClass(color_logger.ColorLogger)
    log = logging.getLogger(__file__[:-3])
    log.setLevel(logging.DEBUG)

    log.debug("AAA")
    log.info("AAA")
    log.warning("AAA")
    log.error("AAA")
    log.critical("AAA")

    log.debug("%s, %s", "Hello", "World")
    log.info("%s, %s", "Hello", "World")
    log.warning("%s, %s", "Hello", "World")
    log.error("%s, %s", "Hello", "World")
    log.critical("%s, %s", "Hello", "World")

    cprint("Hello", Colors.RED)
    cprint("World", Colors.GREEN)
    cprint("0", Colors.BLUE)
    cprint("1", Colors.CYAN)
    cprint("2", Colors.YELLOW)
    cprint("3", Colors.RESET)

    # Disabling color output:
    color_logger.color_logger.use_color = False
    cprint("Hello", '\033[31m')
    log.critical("AAA")


if __name__ == "__main__":
    test_all_functions()
