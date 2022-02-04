from telegram.ext import MessageFilter
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from abc import abstractmethod
from Handlers.ReplyFormatter import ReplyFormatter


class CommandHandler(MessageFilter):

    def __init__(self):
        self.reply_formatter = ReplyFormatter()

    @abstractmethod
    def filter(self, message):
        return

    @abstractmethod
    def handle_command(self, update: Update, context: CallbackContext):
        return

    def reply_message_builder(self, nearestCashiers):
        return self.reply_formatter.nearest_banks_reply(nearestCashiers)

    def link_builder(self, usersPosition, nearestCashiers):
        return self.reply_formatter.image_link_reply(usersPosition,nearestCashiers)
