import contextlib
import psycopg2
from config import DATABASE_URL


@contextlib.contextmanager
def get_postgres_cursor():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        yield cur
    except Exception as exception:
        print(exception)
    finally:
        conn.close()
