import duckdb as db

conn = db.connect('jaffle_shop_db.duckdb')


conn.execute('CREATE SCHEMA IF NOT EXISTS jaffle_raw')

conn.execute('USE jaffle_raw')

conn.execute('CREATE TABLE IF NOT EXISTS raw_customers AS SELECT * FROM "./data/raw_customers.csv"')

conn.execute('CREATE TABLE IF NOT EXISTS raw_orders AS SELECT * FROM "./data/raw_orders.csv"')

conn.execute('CREATE TABLE IF NOT EXISTS raw_payments AS SELECT * FROM "./data/raw_payments.csv"')


conn.sql("SHOW TABLES")