from geolib import geohash
from Model.PostgresConnection import get_postgres_cursor
from constants import GEOHASH_PRECISION

EXTRACTION_LIMIT = 1000.0


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
        return self.extractions < EXTRACTION_LIMIT

    def calculate_geohash(self):
        return geohash.encode(self.latitude, self.longitude, GEOHASH_PRECISION)

    def load_cashier(self):
        query = "UPDATE available_cashiers SET extractions_done 0 WHERE id = %s;"
        with get_postgres_cursor() as cursor:
            cursor.execute(query, (self.id,))

        self.extractions = 0

    def is_not_available(self):
        return not self.is_available()

    def is_available(self):
        return self.__can_extract_money() and self.__is_in_caba()

    def get_bank_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def use_cashier(self, probabilityOfExtraction):
        query = "UPDATE available_cashiers SET extractions_done = extractions_done + %s WHERE id = %s;"
        with get_postgres_cursor() as cursor:
            cursor.execute(query, (probabilityOfExtraction, self.id))
