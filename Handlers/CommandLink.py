from Handlers.Command import CommandHandler
import re

LATITUDE = 1
LONGITUDE = 2


class CommandLink(CommandHandler):

    def __init__(self, nearestCashiers):
        super().__init__()
        self.nearest_cashiers = nearestCashiers

    def filter(self, message):
        return bool(re.search("/link", message.text, re.IGNORECASE))

    def get_nearest_cashiers(self, latitude, longitude):
        return self.nearest_cashiers.get_nearest_link_cashiers(
            float(latitude), float(longitude))

