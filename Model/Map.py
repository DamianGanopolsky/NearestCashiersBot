from ProximityHashes import get_geohashes_neighbours
import csv
from Model.Cashier import Cashier
import psycopg2
from config import DATABASE_URL


class Map:
    def __init__(self, typeOfBank):
        self.locations = {}
        self.cashiers = []
        self.banks_initial_extractions = {}
        self.__cashiers_initial_extractions()
        self.__load(typeOfBank)

    def update(self):
        for cashier in self.cashiers:
            if cashier.is_not_available() and (cashier in self.locations[cashier.calculate_geohash()]):
                self.locations[cashier.calculate_geohash()].remove(cashier)

    def __bulk_update(self):
        self.locations.clear()
        for cashier in self.cashiers:
            if cashier.is_available():
                self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)

    def load_cashiers(self):
        for cashier in self.cashiers:
            cashier.load_cashier()

        self.__bulk_update()

    def __cashiers_initial_extractions(self):
        conn = psycopg2.connect(DATABASE_URL)
        conn.set_session(autocommit=True)

        cur = conn.cursor()

        cur.execute("""
            SELECT c.id,c.extractions_done FROM available_cashiers c;
         """)

        query_result = cur.fetchall()

        for cashier in query_result:
            self.banks_initial_extractions[cashier[0]] = cashier[1]

        conn.close()

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

                cashier = Cashier(row, self.banks_initial_extractions[int(row[0])])

                self.cashiers.append(cashier)

                if self.banks_initial_extractions[int(row[0])] >= 1000.0:
                    continue

                self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)

    def get_nearest_cashiers(self, queryLatitude, queryLongitude):
        proximity_geohashes = get_geohashes_neighbours(queryLatitude, queryLongitude, 500, 7).split(",")
        nearest_banks = []
        count = 0
        for proximityHash in proximity_geohashes:
            if proximityHash in self.locations:
                for bank in self.locations[proximityHash]:
                    nearest_banks.append(bank)
                    count += 1
                    if count >= 3:
                        return nearest_banks

        if count == 0:
            return "There are no banks nearby"
