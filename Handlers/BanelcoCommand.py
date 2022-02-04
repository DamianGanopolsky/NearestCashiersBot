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

    def link_builder(self, usersPosition, nearestCashiers):
        link = "https://maps.googleapis.com/maps/api/staticmap?zoom=16&size=600x300&maptype=roadmap&markers=color:red|"\
               + usersPosition[1]+","+usersPosition[2]

        colors = ["green|","blue|","yellow|"]
        colourSelector = 0
        for cashier in nearestCashiers:
            print("Cashier longitud:",cashier[2])
            print("Cashier latitud:",cashier[3])
            link += "&markers=color:"+ colors[colourSelector] + cashier[2]+","+ cashier[3]
            colourSelector += 1

        link += "&key=AIzaSyD2gw4CTUJCUw6-CmRDHWL2oZXbOdvwej8"
        return link

    def handlerBanelcoCommand(self, update: Update, context: CallbackContext):
        message_info = self.message.split(" ")

        nearest_cashiers = self.nearest_cashiers.get_nearest_banelco_cashiers(
            float(message_info[1]), float(message_info[2]))

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=nearest_cashiers)
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo = self.link_builder(message_info,nearest_cashiers))
