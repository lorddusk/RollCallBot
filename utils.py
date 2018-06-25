import os
import sys

def checkForConfig(logger):
    if os.path.exists('config.ini'):
        pass
    else:
        f = open('config.ini', 'w+')
        f.write('[config]\ntoken = REPLACE_ME_WITH_TOKEN')
        f.close()
        logger.info("Config.ini generated, please fill that in and restart the bot.")
        sys.exit()
