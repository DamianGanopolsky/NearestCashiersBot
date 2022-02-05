from Model.Map import Map


class NearestCashiers:

    def __init__(self):
        self.link_geo_map = Map("LINK")
        self.banelco_geo_map = Map("BANELCO")

    def get_nearest_link_cashiers(self, latitude, longitude):
        return self.link_geo_map.get_nearest_cashiers(latitude, longitude)

    def get_nearest_banelco_cashiers(self, latitude, longitude):
        return self.banelco_geo_map.get_nearest_cashiers(latitude, longitude)

    def update_database(self,nearest_cashiers):
        pass
