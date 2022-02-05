from Model.Map import Map

EXTRACTION_PROBABILITY = [0.7, 0.2, 0.1]


class NearestCashiers:

    def __init__(self):
        self.link_geo_map = Map("LINK")
        self.banelco_geo_map = Map("BANELCO")
        self.maps = [self.link_geo_map, self.banelco_geo_map]

    def get_nearest_link_cashiers(self, latitude, longitude):
        return self.link_geo_map.get_nearest_cashiers(latitude, longitude)

    def get_nearest_banelco_cashiers(self, latitude, longitude):
        return self.banelco_geo_map.get_nearest_cashiers(latitude, longitude)

    def load_cashiers(self):
        map(lambda x: x.load_cashiers(), self.maps)

    def update_available_cashiers(self, cashiersUsed):
        i = 0
        for cashier in cashiersUsed:
            cashier.use_cashier(EXTRACTION_PROBABILITY[i])
            i += 1

        map(lambda x: x.update(), self.maps)
