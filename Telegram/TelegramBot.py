from telegram.ext import Updater, MessageHandler
from Handlers.CommandLink import CommandLink
from Handlers.CommandBanelco import CommandBanelco
from Model.NearestCashiers import NearestCashiers
from Handlers.TextMessageHandler import TextMessage


def run():
    updater = Updater(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA', use_context=True)
    dispatcher = updater.dispatcher

    nearest_cashiers = NearestCashiers()
    link_command = CommandLink(nearest_cashiers)
    banelco_command = CommandBanelco(nearest_cashiers)
    text_message_handler = TextMessage()

    dispatcher.add_handler(MessageHandler(link_command, link_command.handle_command))
    dispatcher.add_handler(MessageHandler(banelco_command, banelco_command.handle_command))
    dispatcher.add_handler(MessageHandler(text_message_handler, text_message_handler.reply))

    updater.start_polling()
    updater.idle()
