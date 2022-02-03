from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
import telegram
from telegram.ext import Updater



updater = Updater(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA', use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text = "Im a bot")

def run():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()