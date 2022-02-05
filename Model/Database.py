conn = psycopg2.connect(DATABASE_URL)
conn.set_session(autocommit=True)

cur = conn.cursor()

cur.execute("""
    UPDATE available_cashiers SET extractions_done 0 WHERE id = %s;
""", (self.id,))



import psycopg2
from config import DATABASE_URL

class PostgresConnection(object):


    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect(DATABASE_URL)

    def __exit__(self):
        self.conn.close()