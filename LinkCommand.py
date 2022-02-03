from telegram.ext import MessageFilter
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
import re

class FilterLink(MessageFilter):
    def filter(self,message):
        return bool(re.search("/link", message.text, re.IGNORECASE))

    def handlerLinkCommand(self,update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="COMMAND LINK")