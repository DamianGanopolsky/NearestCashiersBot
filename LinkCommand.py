from telegram.ext import MessageFilter
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update

class FilterLink(MessageFilter):
    def filter(self,message):
        return 'link'  in message.text

    def handlerLinkCommand(self,update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="COMMAND LINK")