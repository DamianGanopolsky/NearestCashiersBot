from ProximityHashes import get_geohashes_neighbours
import csv
from Model.Cashier import Cashier
import psycopg2

class Map:
    def __init__(self, typeOfBank):
        self.locations = {}
        self.banks_without_extractions = []
        self.__banks_without_extractions()
        self.__load(typeOfBank)

    def __add_cashier(self, cashier):
        self.locations.setdefault(cashier.calculate_geohash(), []).append(cashier)

    def __banks_without_extractions(self):
        conn = psycopg2.connect(dbname="de09lfgj5gf1st",
                                user="djpqkqkqhawjtt",
                                password="728a8912bc32051c4283efcd99398ceacb1e413da968a200f5ba8a2880be1f17",
                                host="ec2-184-73-25-2.compute-1.amazonaws.com",
                                port="5432"
                                )
        conn.set_session(autocommit=True)

        cur = conn.cursor()

        cur.execute("""
            SELECT c.id FROM available_cashiers c WHERE c.extractions_done > 2.0;
         """)

        query_result = cur.fetchall()

        for i in range(len(query_result)):
            self.banks_without_extractions.append(int(query_result[i][0]))

        conn.close()
        print("Bancos sin extraccion:",self.banks_without_extractions)




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
                if int(row[0]) in self.banks_without_extractions:
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
