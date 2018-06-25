from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler, Updater, ConversationHandler, \
    RegexHandler
from configparser import ConfigParser
from utils import *
from botCommands import *
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
config = ConfigParser()
checkForConfig(logger)
config.read('config.ini')
token = config.get('config', 'token')
updater = Updater(token=token)
job = updater.job_queue
dp = updater.dispatcher

start_handler = CommandHandler('start', start)
start_roll_call_handler = CommandHandler('start_roll_call', start)
end_handler = CommandHandler('end', end)
end_roll_call_handler = CommandHandler('end_roll_call', end)
in_handler = CommandHandler('in', call_in)
out_handler = CommandHandler('out', call_out)
maybe_handler = CommandHandler('maybe', maybe)
who_is_in_handler = CommandHandler('who_is_in', who_is_in)
set_title_handler = CommandHandler('set_title', set_title)
set_in_handler = CommandHandler('set_in_for', set_in_for)
set_out_handler = CommandHandler('set_out_for', set_out_for)
set_maybe_handler = CommandHandler('set_maybe_for', set_maybe_for)
shh_handler = CommandHandler('shh', shh)
louder_handler = CommandHandler('louder', louder)

dp.add_handler(start_handler)
dp.add_handler(start_roll_call_handler)
dp.add_handler(end_handler)
dp.add_handler(end_roll_call_handler)
dp.add_handler(in_handler)
dp.add_handler(out_handler)
dp.add_handler(maybe_handler)
dp.add_handler(who_is_in_handler)
dp.add_handler(set_title_handler)
dp.add_handler(set_in_handler)
dp.add_handler(set_out_handler)
dp.add_handler(set_maybe_handler)
dp.add_handler(shh_handler)
dp.add_handler(louder_handler)

dp.add_error_handler(error)

updater.start_polling(poll_interval=1.0, timeout=20)
updater.idle()

"""Basic Commands
/start_roll_call - Start a new roll call (with optional title)
/end_roll_call - End the current roll call
/in - Let everyone know you'll be attending (with optional comment)
/out - Let everyone know you won't be attending (with optional comment)
/maybe - Let everyone know that you don't know (with optional comment)
/whos_in - List attendees
Other Commands
/set_title {title} - Add a title to the current roll call
/set_in_for {name} - Allows you to respond for another user
/set_out_for {name} - Allows you to respond for another user
/set_maybe_for {name} - Allows you to respond for another user
/shh - Tells WhosInBot not to list all attendees after every response
/louder - Tells WhosInBot to list all attendees after every response"""
