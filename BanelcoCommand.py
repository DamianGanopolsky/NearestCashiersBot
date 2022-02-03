from telegram.ext import MessageFilter
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
import re

class BanelcoHandler(MessageFilter):
    def filter(self,message):
        return bool(re.search("/banelco", message.text, re.IGNORECASE))
        #return 'banelco'  in message.text


    def handlerBanelcoCommand(self,update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="COMMAND BANELCO")


