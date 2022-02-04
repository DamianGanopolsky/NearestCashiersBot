from ProximityHashes import get_geohashes_neighbours
import csv
from Model.Cashier import Cashier


class Map:
    def __init__(self, typeOfBank):
        self.locations = {}
        self.__load(typeOfBank)

    def __add_cashier(self, cashier):
        self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)

    def __load(self, typeOfBank):
        with open('cajeros-automaticos.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            row_count = 0

            for row in csv_reader:
                row_count += 1
                if row_count == 1:
                    continue
                if row[6] != 'CABA':
                    continue
                if row[4] != typeOfBank:
                    continue
                cashier = Cashier(row)
                self.__add_cashier(cashier);

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
