import rollcall
import json
from pathlib import Path

def startRollCall(update):
    message = update.message
    title = message.text.split(' ', 1)
    if len(title) > 1:
        title = message.text.split(' ', 1)[1]
    else:
        title = ''
    chat_id = message.chat.id
    r = rollcall.Rollcall(chat_id, title, [])
    with open('json/chats/' + str(chat_id) + '.json', 'w') as outfile:
        outfile.write(str(r.toJSON()))
        message.reply_text('Roll call started')


def inMessage(update):
    message = update.message
    title = message.text.split(' ', 1)
    if len(title) > 1:
        title = message.text.split(' ', 1)[1]
    else:
        title = ''
    chat_id = message.chat.id
    username = message.chat.username
    if checkForChat(chat_id):
        chatter = message.from_user.first_name
        u = rollcall.User(chatter, username , 1, title)
        with open('json/chats/' + str(chat_id) + '.json') as f:
            r = json.load(f)
            r = rollcall.Rollcall(**r)
            r.users.append(u)
            with open('json/chats/' + str(chat_id) + '.json', 'w') as outfile:
                outfile.write(r.toJSON())
        message.reply_text('Set as in')
    else:
        message.reply_text("Roll call hasn't started yet.")


def checkForChat(chat_id):
    file = Path('json/chats/' + str(chat_id) + '.json')
    if file.exists():
        return True
    else:
        return False
