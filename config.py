POSTGRES_DB = "de09lfgj5gf1st"
POSTGRES_USER = "djpqkqkqhawjtt"
POSTGRES_PASSWORD = "728a8912bc32051c4283efcd99398ceacb1e413da968a200f5ba8a2880be1f17"
POSTGRES_HOST = "ec2-184-73-25-2.compute-1.amazonaws.com"
POSTGRES_PORT = "5432"

DATABASE_URL = "dbname=%s user=%s password=%s host=%s port=%s" % (POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
                                                                  , POSTGRES_HOST, POSTGRES_PORT)
