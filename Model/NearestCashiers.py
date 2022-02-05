from Model.Map import Map


class NearestCashiers:

    def __init__(self):
        self.link_geo_map = Map("LINK")
        self.banelco_geo_map = Map("BANELCO")

    def get_nearest_link_cashiers(self, latitude, longitude):
        return self.link_geo_map.get_nearest_cashiers(latitude, longitude)

    def get_nearest_banelco_cashiers(self, latitude, longitude):
        return self.banelco_geo_map.get_nearest_cashiers(latitude, longitude)

    def load_cashiers(self):
        self.link_geo_map.load_cashiers()
        self.banelco_geo_map.load_cashiers()

    def update_available_cashiers(self, cashiersUsed):

        probability_of_extraction = [0.7, 0.2, 0.1]

        i = 0
        for cashier in cashiersUsed:
            cashier.is_used_with_prob(probability_of_extraction[i])
            i += 1

        self.link_geo_map.update()
        self.banelco_geo_map.update()
