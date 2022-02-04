from geolib import geohash


class Cashier:

    def __init__(self, data):
        self.longitude = data[1]
        self.latitude = data[2]
        self.name = data[3]
        self.type = data[4]
        self.address = data[10] + ' ' + data[11]

    def get_data(self):
        return self.name, self.address

    def calculate_geohash(self):
        return geohash.encode(self.latitude, self.longitude, 7)
