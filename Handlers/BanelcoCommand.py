from telegram.ext import MessageFilter
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
import re


class BanelcoHandler(MessageFilter):

    def __init__(self, nearestCashiers):
        self.nearest_cashiers = nearestCashiers
        self.message = ""

    def filter(self, message):
        self.message = message.text
        return bool(re.search("/banelco", message.text, re.IGNORECASE))

    def handlerBanelcoCommand(self, update: Update, context: CallbackContext):
        print("Message es",self.message)
        message_info = self.message.split(" ")

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=self.nearest_cashiers.get_nearest_banelco_cashiers(
                                     float(message_info[1]), float(message_info[2])
                                 ))
