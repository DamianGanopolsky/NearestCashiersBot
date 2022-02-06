from telegram import Update
from telegram.ext import CallbackContext, Filters,  MessageFilter


class TextMessage(MessageFilter):

    def filter(self, message):
        return Filters.text & (~Filters.command)

    def reply(self, update: Update, context: CallbackContext):
        context.bot.send_message \
            (chat_id=update.effective_chat.id, text="""Hi! I'm the NearestCashiersBot.
Available commands:
            /link [latitude] [longitude]: lists 3 Link cashiers within 500m
            /banelco [latitude] [longitude]: lists 3 Banelco cashiers within 500m
            """
             )
