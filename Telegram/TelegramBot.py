from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters
from Handlers.CommandLink import CommandLink
from Handlers.CommandBanelco import CommandBanelco
from Model.NearestCashiers import NearestCashiers


updater = Updater(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA', use_context=True)
dispatcher = updater.dispatcher


def echo(update: Update, context: CallbackContext):
    context.bot.send_message \
        (chat_id=update.effective_chat.id, text="""Hi! I'm the NearestCashiersBot.
        Available commands:
        /link [latitude] [longitude]: lists the 3 nearest Link cashiers
        /banelco [latitude] [longitude]: lists the 3 nearest Banelco cashiers
        """
         )


def run():

    nearest_cashiers = NearestCashiers()
    link_filter = CommandLink(nearest_cashiers)
    banelco_command = CommandBanelco(nearest_cashiers)

    dispatcher.add_handler(MessageHandler(link_filter, link_filter.handle_command))
    dispatcher.add_handler(MessageHandler(banelco_command, banelco_command.handle_command))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    updater.start_polling()

    updater.idle()
