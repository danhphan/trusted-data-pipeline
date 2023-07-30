import duckdb as db
import pandas as pd

def create_raw_scheme():
    conn = db.connect('jaffle_shop_db.duckdb')
    conn.execute('CREATE SCHEMA IF NOT EXISTS jaffle_raw')
    conn.execute('USE jaffle_raw')
    return conn


conn = db.connect('jaffle_shop_db.duckdb')

conn.execute('CREATE SCHEMA jaffle_raw')

conn.execute('USE jaffle_raw')


def extract_raw_customers():
    df = pd.read_csv("s3://dbt-tutorial-public/jaffle_shop_customers.csv")
    return df


def load_raw_customers():
    conn = create_raw_scheme()
    conn.execute('CREATE TABLE raw_customers AS SELECT * FROM "./data/raw_customers.csv"')



conn.execute('CREATE TABLE raw_customers AS SELECT * FROM "./data/raw_customers.csv"')

conn.execute('CREATE TABLE raw_orders AS SELECT * FROM "./data/raw_orders.csv"')

conn.execute('CREATE TABLE raw_payments AS SELECT * FROM "./data/raw_payments.csv"')


# conn.execute('CREATE SCHEMA IF NOT EXISTS jaffle_raw')

# conn.execute('USE jaffle_raw')

# conn.execute('CREATE TABLE IF NOT EXISTS raw_customers AS SELECT * FROM "./data/raw_customers.csv"')

# conn.execute('CREATE TABLE IF NOT EXISTS raw_orders AS SELECT * FROM "./data/raw_orders.csv"')

# conn.execute('CREATE TABLE IF NOT EXISTS raw_payments AS SELECT * FROM "./data/raw_payments.csv"')


conn.sql("SHOW TABLES")