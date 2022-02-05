from Model.Map import Map
import psycopg2
from config import DATABASE_URL

class NearestCashiers:

    def __init__(self):
        self.link_geo_map = Map("LINK")
        self.banelco_geo_map = Map("BANELCO")

    def get_nearest_link_cashiers(self, latitude, longitude):
        return self.link_geo_map.get_nearest_cashiers(latitude, longitude)

    def get_nearest_banelco_cashiers(self, latitude, longitude):
        return self.banelco_geo_map.get_nearest_cashiers(latitude, longitude)

    def update_available_cashiers(self, cashiersUsed):
        conn = psycopg2.connect(DATABASE_URL)
        conn.set_session(autocommit=True)

        cur = conn.cursor()

        probability_of_extraction = [0.7, 0.2, 0.1]

        #for i in range(len(cashiersUsed)):
         #   cur.execute("""
          #      UPDATE available_cashiers SET extractions_done = extractions_done + %s WHERE id = %s;
           #  """, (probability_of_extraction[i], cashiersUsed[i][4]))

        conn.close()

        self.link_geo_map.update()
        self.banelco_geo_map.update()
