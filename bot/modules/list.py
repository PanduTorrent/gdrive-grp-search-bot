from telegram.ext import CommandHandler, run_async
from bot.helper.drive_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands

@run_async
def list_drive(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
    except IndexError:
        sendMessage('<b>Send a search query along with command. \nLike this /search the_thing_you_want</b>', context.bot, update)
        return
        
    reply = sendMessage('<b>Searching the Database...  🌍🌎🌏\n╾───────────────────────────────╼\nSearching the files might take some time to complete \nas it is searching in multiple TDs (50-60).\nSo pls be patient, and wait 2-3 minutes \nbefore sending the Search query again.\nAnd pls  🥺  dont spam the BOT. \n╾───────────────────────────────╼\n<code>The Result is worth the Wait.</code></b>', context.bot, update)

    LOGGER.info(f"Searching: {search}")
        
    gdrive = GoogleDriveHelper(None)
    msg, button = gdrive.drive_list(search)

    editMessage(msg,reply,button)


list_handler = CommandHandler(BotCommands.ListCommand, list_drive,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(list_handler)
