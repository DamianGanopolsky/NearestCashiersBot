LATITUDE = 1
LONGITUDE = 2
BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?zoom=15&size=600x300&maptype=roadmap&markers=color:red|"
GOOGLE_TOKEN = "AIzaSyD2gw4CTUJCUw6-CmRDHWL2oZXbOdvwej8"
COLORS = ["green|", "blue|", "yellow|"]

class ReplyFormatter:

    def nearest_banks_reply(self, nearestCashiers):
        reply = "Cashiers within 500m:"

        for cashier in nearestCashiers:
            reply += "\n\n Bank name: " + cashier.get_bank_name() + "\n Address: " + cashier.get_address()

        return reply

    def image_link_reply(self, usersPosition, nearestCashiers):
        link = BASE_URL + usersPosition[LATITUDE] + "," + usersPosition[LONGITUDE]

        color_selector = 0
        for cashier in nearestCashiers:
            link += "&markers=color:" + COLORS[color_selector] + cashier.get_latitude() + "," \
                    + cashier.get_longitude()
            color_selector += 1

        link += "&key=" + GOOGLE_TOKEN
        return link
