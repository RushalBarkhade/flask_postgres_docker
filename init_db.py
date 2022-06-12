import os
import psycopg2

def get_db_connection():
    POST_URL = "host={} dbname={} user={} password={}".format(os.getenv("POSTGRES_HOST"),os.getenv("POSTGRES_DB"),os.getenv("POSTGRES_USER"),os.getenv("POSTGRES_PASSWORD"),os.getenv("POSTGRES_PORT"))
    conn = psycopg2.connect(POST_URL)
    return conn