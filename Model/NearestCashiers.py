import csv
from Model.Cashier import Cashier
from Model.Map import Map


class NearestCashiers:

    def __init__(self):
        self.geo_map = Map()
        self.__load_map()
        pass

    def get_nearest_cashiers(self):
        return self.geo_map.get_nearest_cashiers(-34.56422521903438, -58.458954944959636)

    def __load_map(self):
        with open('cajeros-automaticos.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0

            for row in csv_reader:
                line_count += 1
                if line_count == 1:
                    continue
                if row[6] != 'CABA':
                    continue
                cashier = Cashier(row)
                self.geo_map.add_cashier(cashier);
