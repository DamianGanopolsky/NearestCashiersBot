import csv
from Model.Cashier import Cashier
from Model.PostgresConnection import get_postgres_cursor
from constants import FIELDS, DATASET_FILE

CASHIER_ID = 0
EXTRACTIONS = 1


class Loader:

    def __init__(self):
        self.banks_initial_extractions = {}

    def __get_extractions_from_db(self):
        with get_postgres_cursor() as cursor:
            cursor.execute("""
                SELECT c.id,c.extractions_done FROM available_cashiers c;
             """)
            query_result = cursor.fetchall()

        for cashier in query_result:
            self.banks_initial_extractions[cashier[CASHIER_ID]] = cashier[EXTRACTIONS]

    def __get_cashiers_from_file(self, typeOfBank):
        cashiers = []
        with open(DATASET_FILE) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for row in csv_reader:

                if row[FIELDS["CASHIER_TYPE"]] != typeOfBank:
                    continue
                cashier = Cashier(row, self.banks_initial_extractions[int(row[FIELDS["ID"]])])
                cashiers.append(cashier)
        return cashiers

    def load_map_cashiers(self, typeOfBank):
        self.__get_extractions_from_db()
        return self.__get_cashiers_from_file(typeOfBank)
