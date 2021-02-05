import logging
import os
import time

import telegram.ext as tg
from dotenv import load_dotenv

from telegraph import Telegraph

botStartTime = time.time()
if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

load_dotenv('config.env')

def getConfig(name: str):
    return os.environ[name]

LOGGER = logging.getLogger(__name__)

try:
    if bool(getConfig('_____REMOVE_THIS_LINE_____')):
        logging.error('The README.md file there to be read! Exiting now!')
        exit()
except KeyError:
    pass

BOT_TOKEN = None

AUTHORIZED_CHATS = set()

AUTHORIZED_CHATS = set()
if os.path.exists('authorized_chats.txt'):
    with open('authorized_chats.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            AUTHORIZED_CHATS.add(int(line.split()[0]))

try:
    BOT_TOKEN = getConfig('BOT_TOKEN')
    OWNER_ID = int(getConfig('OWNER_ID'))
    telegraph_token = getConfig('TELEGRAPH_TOKEN')
except KeyError as e:
    LOGGER.error("One or more env variables missing! Exiting now")
    exit(1)

DRIVE_NAME = []
DRIVE_ID = []
INDEX_URL = []

if os.path.exists('drive_folder'):
    with open('drive_folder', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            temp = line.strip().split()
            DRIVE_NAME.append(temp[0].replace("_", " "))
            DRIVE_ID.append(temp[1])
            try:
                INDEX_URL.append(temp[2])
            except IndexError as e:
                INDEX_URL.append(None)

if DRIVE_ID :
    pass
else :
    LOGGER.error("The README.md file there to be read! Exiting now!")
    exit(1)

telegra_ph = Telegraph(access_token=telegraph_token)

updater = tg.Updater(token=BOT_TOKEN,use_context=True)
bot = updater.bot
dispatcher = updater.dispatcher
