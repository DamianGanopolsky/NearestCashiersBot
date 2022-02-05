from geolib import geohash
from Model.PostgresConnection import get_postgres_cursor


class Cashier:

    def __init__(self, data, initialStatus):
        self.id = data[0]
        self.longitude = data[1]
        self.latitude = data[2]
        self.name = data[3]
        self.type = data[4]
        self.address = data[5]
        self.state = data[6]
        self.extractions = initialStatus

    def __is_in_caba(self):
        return self.state == "CABA"

    def __can_extract_money(self):
        return self.extractions < 1000.0

    def get_data(self):
        return self.name, self.address, self.latitude, self.longitude, self.id

    def calculate_geohash(self):
        return geohash.encode(self.latitude, self.longitude, 7)

    def load_cashier(self):
        with get_postgres_cursor() as cur:
            cur.execute("""
                UPDATE available_cashiers SET extractions_done 0 WHERE id = %s;
            """, (self.id,))

        self.extractions = 0

    def is_not_available(self):
        return not self.is_available()

    def is_available(self):
        return self.__can_extract_money() and self.__is_in_caba()

    def is_used_with_prob(self, probabilityOfExtraction):
        with get_postgres_cursor() as cur:
            cur.execute("""
                    UPDATE available_cashiers SET extractions_done = extractions_done + %s WHERE id = %s;
            """, (probabilityOfExtraction, self.id))
