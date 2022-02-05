from Model.Map import Map
import psycopg2


class NearestCashiers:

    def __init__(self):
        self.link_geo_map = Map("LINK")
        self.banelco_geo_map = Map("BANELCO")

    def get_nearest_link_cashiers(self, latitude, longitude):
        return self.link_geo_map.get_nearest_cashiers(latitude, longitude)

    def get_nearest_banelco_cashiers(self, latitude, longitude):
        return self.banelco_geo_map.get_nearest_cashiers(latitude, longitude)

    def update_database(self, nearest_cashiers):
        conn = psycopg2.connect(dbname="de09lfgj5gf1st",
                                user="djpqkqkqhawjtt",
                                password="728a8912bc32051c4283efcd99398ceacb1e413da968a200f5ba8a2880be1f17",
                                host="ec2-184-73-25-2.compute-1.amazonaws.com",
                                port="5432"
                                )
        conn.set_session(autocommit=True)

        cur = conn.cursor()

        probability_of_extraction = [0.7, 0.2, 0.1]

        for i in range(len(nearest_cashiers)):
            cur.execute("""
                UPDATE available_cashiers SET extractions_done = extractions_done + %s WHERE id = %s;
             """, (probability_of_extraction[i], nearest_cashiers[i][4]))

        conn.close()
