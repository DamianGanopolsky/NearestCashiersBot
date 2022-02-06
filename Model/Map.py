from ProximityHashes import get_geohashes_neighbours
from Model.Loader import Loader
from constants import GEOHASH_PRECISION

GEOHASH_RADIUS = 500


class Map:
    def __init__(self, typeOfBank):
        self.locations = {}
        self.cashiers = Loader().load_map_cashiers(typeOfBank)
        self.__bulk_update()

    def __bulk_update(self):
        self.locations.clear()
        for cashier in self.cashiers:
            if cashier.is_available():
                self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)

    def update(self):
        for cashier in self.cashiers:
            if cashier.is_not_available() and (cashier.calculate_geohash() in self.locations) \
                    and (cashier in self.locations[cashier.calculate_geohash()]):
                self.locations[cashier.calculate_geohash()].remove(cashier)

    def load_cashiers(self):
        for cashier in self.cashiers:
            cashier.load_cashier()
        self.__bulk_update()

    def get_nearest_cashiers(self, queryLatitude, queryLongitude):
        proximity_geohashes = get_geohashes_neighbours \
            (queryLatitude, queryLongitude, GEOHASH_RADIUS, GEOHASH_PRECISION).split(",")
        nearest_banks = []
        count = 0
        for proximityHash in proximity_geohashes:
            if proximityHash in self.locations:
                for bank in self.locations[proximityHash]:
                    nearest_banks.append(bank)
                    count += 1
                    if count >= 3:
                        return nearest_banks

        return nearest_banks
