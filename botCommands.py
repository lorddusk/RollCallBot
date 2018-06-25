import logging
from botFunctions import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    logger.info("start")
    startRollCall(update)


def end(bot, update):
    logger.info("end")


def call_in(bot, update):
    logger.info("in")
    inMessage(update)



def call_out(bot, update):
    logger.info("out")


def maybe(bot, update):
    logger.info("maybe")


def who_is_in(bot, update):
    logger.info("who_is_in")


def set_title(bot, update):
    logger.info("set_title")


def set_in_for(bot, update):
    logger.info("set_in_for")


def set_out_for(bot, update):
    logger.info("set_out_for")


def set_maybe_for(bot, update):
    logger.info("set_maybe_for")


def shh(bot, update):
    logger.info("shh")


def louder(bot, update):
    logger.info("louder")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)