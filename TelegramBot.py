from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
import telegram


updater = Updater(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA', use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text = "The command is being executed")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message\
        (chat_id=update.effective_chat.id, text = """Hi! I'm the NearestCashiersBot.
        Available commands:
        /link : lists the 3 nearest Link cashiers
        /Banelco: lists the 3 nearest Banelco cashiers
        """
                                                                )

def run():
    start_handler = CommandHandler('start', start)
    echo_handler =  MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_handler)
    updater.start_polling()