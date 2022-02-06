from Handlers.Command import CommandHandler
import re

LATITUDE = 1
LONGITUDE = 2


class CommandBanelco(CommandHandler):

    def __init__(self, nearestCashiersModel):
        super().__init__(nearestCashiersModel)

    def filter(self, message):
        return bool(re.search("/banelco", message.text, re.IGNORECASE))

    def get_nearest_cashiers(self, latitude, longitude):
        return self.model.get_nearest_banelco_cashiers(float(latitude), float(longitude))
