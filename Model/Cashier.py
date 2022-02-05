from geolib import geohash


class Cashier:

    def __init__(self, data):
        self.id = data[0]
        self.longitude = data[1]
        self.latitude = data[2]
        self.name = data[3]
        self.type = data[4]
        self.address = data[5]

    def get_data(self):
        return self.name, self.address, self.latitude, self.longitude, self.id

    def calculate_geohash(self):
        return geohash.encode(self.latitude, self.longitude, 7)

    def is_used_with_prob(self):
        pass
