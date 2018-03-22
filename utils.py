import os
import sys
import sqlite3

conn = sqlite3.connect('rollcalls.db', check_same_thread=False)


def initDatabase():
    executeQuery("CREATE TABLE IF NOT EXISTS Rollcalls (ID INTEGER PRIMARY KEY NOT NULL, CHAT INTEGER NOT NULL, TITLE CHAR(1024) NOT NULL, STATUS INTEGER NOT NULL)")
    conn.commit()


def checkForConfig(logger):
    if os.path.exists('config.ini'):
        pass
    else:
        f = open('config.ini', 'w+')
        f.write('[config]\ntoken = REPLACE_ME_WITH_TOKEN')
        f.close()
        logger.info("Config.ini generated, please fill that in and restart the bot.")
        sys.exit()


def executeQuery(query):
    c = conn.cursor()
    c.execute(query)
