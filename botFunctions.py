from utils import *


def startRollCall(message):
    title = message.text.split(' ', 1)
    if len(title) > 1:
        title = message.text.split(' ', 1)[1]
    else:
        title = ''
    chat_id = message.chat.id
    query = "INSERT INTO Rollcalls(CHAT,TITLE,STATUS) VALUES (" + str(chat_id) + ",'" + str(title) + "',1)"
    print(query)
    executeQuery(query)
