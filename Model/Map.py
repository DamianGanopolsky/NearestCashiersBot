from ProximityHashes import get_geohashes_neighbours


class Map:
    def __init__(self):
        self.locations = {}

    def add_cashier(self, cashier):
        self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)

    def get_nearest_cashiers(self, queryLatitude, queryLongitude):
        proximity_geohashes = get_geohashes_neighbours(queryLatitude, queryLongitude, 500, 7).split(",")
        nearest_banks = []
        count = 0
        for proximityHash in proximity_geohashes:
            if proximityHash in self.locations:
                for bank in self.locations[proximityHash]:
                    nearest_banks.append(bank.get_data())
                    count += 1
                    if count >= 3:
                        return nearest_banks

        if count == 0:
            return "There are no banks nearby"