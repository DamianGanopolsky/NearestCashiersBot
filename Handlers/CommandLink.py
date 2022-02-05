from telegram.ext import MessageFilter
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from Handlers.CommandHandler import CommandHandler
import re


class CommandLink(CommandHandler):

    def __init__(self, nearestCashiers):
        super().__init__()
        self.nearest_cashiers = nearestCashiers
        self.message = ""

    def filter(self, message):
        self.message = message.text
        return bool(re.search("/link", message.text, re.IGNORECASE))

    def handle_command(self, update: Update, context: CallbackContext):
        message_info = self.message.split(" ")

        nearest_cashiers = self.nearest_cashiers.get_nearest_link_cashiers(
            float(message_info[1]), float(message_info[2]))

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=super().reply_message_builder(nearest_cashiers)
                                 )
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=super().link_builder(message_info, nearest_cashiers))

        self.nearest_cashiers.update_available_cashiers(nearest_cashiers)
