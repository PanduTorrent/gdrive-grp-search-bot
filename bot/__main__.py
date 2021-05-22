from telegram.ext import CommandHandler, run_async
from bot import dispatcher, updater, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list

@run_async
def start(update, context):
    LOGGER.info('UID: {} - UN: {} - MSG: {}'.format(update.message.chat.id,update.message.chat.username,update.message.text))
    if update.message.chat.type == "private" :
        sendMessage(f"Hey! <b>{update.message.chat.first_name}</b>. Welcome to <b>PANDUTORRENTS SEARCH BOT</b>", context.bot, update)
    else :
        sendMessage("Hey! This Bot Searches All Team-Drives. Use /search [Keyword]", context.bot, update)
    if not CustomFilters.authorized_user(update):
        sendMessage("This Bot Only Works with Only Authorized Users", context.bot, update)
        
@run_async
def log(update, context):
    sendLogFile(context.bot, update)

def main():

    start_handler = CommandHandler(BotCommands.StartCommand, start, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(log_handler)

    updater.start_polling()
    LOGGER.info("Yeah am running!")
    updater.idle()

main()
