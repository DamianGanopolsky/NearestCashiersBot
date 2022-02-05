import psycopg2
from config import DATABASE_URL
import csv
from Model.Cashier import Cashier


class Loader:

    def __init__(self):
        self.banks_initial_extractions = {}

    def __get_data_from_db(self):
        try:
            conn = psycopg2.connect(DATABASE_URL)
            conn.set_session(autocommit=True)
            cur = conn.cursor()
            cur.execute("""
                SELECT c.id,c.extractions_done FROM available_cashiers c;
             """)
        except Exception as ex:
            print(ex)
        finally:
            query_result = cur.fetchall()
            for cashier in query_result:
                self.banks_initial_extractions[cashier[0]] = cashier[1]

            conn.close()

    def __read_file(self, typeOfBank):
        cashiers = []
        with open('cajeros-automaticos.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            row_count = 0

            for row in csv_reader:
                row_count += 1
                if row_count == 1:
                    continue

                if row[4] != typeOfBank:
                    continue
                cashier = Cashier(row, self.banks_initial_extractions[int(row[0])])
                cashiers.append(cashier)
        return cashiers

    def load_map_cashiers(self, typeOfBank):
        self.__get_data_from_db()
        return self.__read_file(typeOfBank)
