from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters
from Handlers.LinkCommand import FilterLink
from Handlers.BanelcoCommand import BanelcoHandler
from Model.NearestCashiers import NearestCashiers

updater = Updater(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA', use_context=True)
dispatcher = updater.dispatcher


def echo(update: Update, context: CallbackContext):
    context.bot.send_message \
        (chat_id=update.effective_chat.id, text="""Hi! I'm the NearestCashiersBot.
        Available commands:
        /link : lists the 3 nearest Link cashiers
        /Banelco: lists the 3 nearest Banelco cashiers
        """
         )


def run():
    nearest_cashiers = NearestCashiers()
    link_filter = FilterLink(nearest_cashiers)
    banelco_command = BanelcoHandler()

    dispatcher.add_handler(MessageHandler(link_filter, link_filter.handlerLinkCommand))
    dispatcher.add_handler(MessageHandler(banelco_command, banelco_command.handlerBanelcoCommand))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    updater.start_polling()

    updater.idle()
