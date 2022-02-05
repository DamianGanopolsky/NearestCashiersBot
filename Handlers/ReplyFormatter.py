LATITUDE = 1
LONGITUDE = 2

class ReplyFormatter:

    def nearest_banks_reply(self, nearestCashiers):
        reply = "Cashiers within 500m:"

        for cashier in nearestCashiers:
            reply += "\n\n Bank name: " + cashier.get_data()[0] + "\n Address: " + cashier.get_data()[1]

        return reply


    def image_link_reply(self, usersPosition, nearestCashiers):
        link = "https://maps.googleapis.com/maps/api/staticmap?zoom=15&size=600x300&maptype=roadmap&markers=color:red|" \
               + usersPosition[LATITUDE] + "," + usersPosition[LONGITUDE]

        colors = ["green|", "blue|", "yellow|"]
        color_selector = 0
        for cashier in nearestCashiers:
            link += "&markers=color:" + colors[color_selector] + cashier.get_data()[2] + "," + cashier.get_data()[3]
            color_selector += 1

        link += "&key=AIzaSyD2gw4CTUJCUw6-CmRDHWL2oZXbOdvwej8"
        return link
