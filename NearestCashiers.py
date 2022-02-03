import csv

from geolib import geohash
from ProximityHashes import get_geohashes_neighbours

#bot = telegram.Bot(token='5164707904:AAFXOrlRZpT1FpfVHPP7ak4QYfC-kafWAvA')



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


class Map:
    def __init__(self):
        self.locations = {}

    def add_cashier(self, cashier):
        print("New geohash:", cashier.calculate_geohash())
        self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)
        print("Cashier value now:", self.locations[cashier.calculate_geohash()])

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

    def print_all_cashiers(self):
        for key, value in self.locations.items():
            print(key, value[0].get_data())


def run():
    #print(bot.get_me())
    #updates = bot.get_updates()
    geo_map = Map()
    with open('cajeros-automaticos.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0

        # En row voy a tener cada fila del csv
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            if line_count > 5:
                break

            if row[6] != 'CABA':
                continue

            cashier = Cashier(row)
            geo_map.add_cashier(cashier);

    print(geo_map.get_nearest_cashiers(-34.6050839250446, -58.3709757833981))
    count=0
    #while True:
     #   count += 1






