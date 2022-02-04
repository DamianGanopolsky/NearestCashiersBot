

class ReplyFormatter:

    def nearest_banks_reply(self, nearestCashiers):
        return ("Cashiers within 500m:\n Bank name: " + nearestCashiers[0][0] + ", Address:" +
                                nearestCashiers[0][1] +"\n Bank name: " + nearestCashiers[1][0]
                                 + ", Address:" + nearestCashiers[1][1] + "\n Bank name: " + nearestCashiers[2][0]
                                 + ", Address:" + nearestCashiers[2][1])

    def image_link_reply(self, usersPosition, nearestCashiers):
        link = "https://maps.googleapis.com/maps/api/staticmap?zoom=14&size=600x300&maptype=roadmap&markers=color:red|" \
               + usersPosition[1] + "," + usersPosition[2]

        colors = ["green|", "blue|", "yellow|"]
        color_selector = 0
        for cashier in nearestCashiers:
            link += "&markers=color:" + colors[color_selector] + cashier[2] + "," + cashier[3]
            color_selector += 1

        link += "&key=AIzaSyD2gw4CTUJCUw6-CmRDHWL2oZXbOdvwej8"
        return link