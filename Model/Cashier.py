from geolib import geohash
import psycopg2
from config import DATABASE_URL


class Cashier:

    def __init__(self, data, initialStatus):
        self.id = data[0]
        self.longitude = data[1]
        self.latitude = data[2]
        self.name = data[3]
        self.type = data[4]
        self.address = data[5]
        self.extractions = initialStatus

    def get_data(self):
        return self.name, self.address, self.latitude, self.longitude, self.id

    def calculate_geohash(self):
        return geohash.encode(self.latitude, self.longitude, 7)

    def load_cashier(self):
        conn = psycopg2.connect(DATABASE_URL)
        conn.set_session(autocommit=True)

        cur = conn.cursor()

        cur.execute("""
            UPDATE available_cashiers SET extractions_done 0 WHERE id = %s;
        """, (self.id,))

        conn.close()
        self.extractions = 0

    def is_not_available(self):
        return self.extractions >= 1000.0

    def is_available(self):
        return self.extractions < 1000.0

    def is_used_with_prob(self, probabilityOfExtraction):
        conn = psycopg2.connect(DATABASE_URL)
        conn.set_session(autocommit=True)

        cur = conn.cursor()

        cur.execute("""
          UPDATE available_cashiers SET extractions_done = extractions_done + %s WHERE id = %s;
      """, (probabilityOfExtraction, self.id))

        conn.close()
