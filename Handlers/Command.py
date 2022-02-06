from telegram.ext import MessageFilter
from telegram.ext import CallbackContext
from telegram import Update
from abc import abstractmethod
from Handlers.ReplyFormatter import ReplyFormatter

LATITUDE = 1
LONGITUDE = 2


class CommandHandler(MessageFilter):

    def __init__(self, nearestCashiersModel):
        self.reply_formatter = ReplyFormatter()
        self.model = nearestCashiersModel

    @abstractmethod
    def filter(self, message):
        return

    def handle_command(self, update: Update, context: CallbackContext):
        message_info = update.message.text.split(" ")

        nearest_cashiers = self.get_nearest_cashiers(message_info[LATITUDE], message_info[LONGITUDE])

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=self.reply_formatter.nearest_banks_reply(nearest_cashiers))

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=self.reply_formatter.image_link_reply(message_info, nearest_cashiers))

        self.model.update_available_cashiers(nearest_cashiers)

