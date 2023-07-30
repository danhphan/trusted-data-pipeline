import duckdb as db
import pandas as pd
import os
from dagster import file_relative_path, asset

DBT_PROJECT_PATH = file_relative_path(__file__, "../../../../dbt_jaffle_shop")

def create_raw_scheme():
    conn = db.connect(f'{DBT_PROJECT_PATH}/jaffle_shop_db.duckdb')
    conn.execute('CREATE SCHEMA IF NOT EXISTS jaffle_raw')
    conn.execute('USE jaffle_raw')
    return conn


@asset
def extract_raw_customers():
    os.makedirs(f"{DBT_PROJECT_PATH}/data", exist_ok=True)
    df = pd.read_csv("s3://dbt-tutorial-public/jaffle_shop_customers.csv")
    df.to_csv(f"{DBT_PROJECT_PATH}/data/raw_customers.csv")


@asset()
def raw_customers(extract_raw_customers):
    conn = create_raw_scheme()
    conn.execute(f'CREATE TABLE IF NOT EXISTS raw_customers AS SELECT * FROM "{DBT_PROJECT_PATH}/data/raw_customers.csv"')

@asset
def extract_raw_orders():
    os.makedirs(f"{DBT_PROJECT_PATH}/data", exist_ok=True)
    df = pd.read_csv("s3://dbt-tutorial-public/jaffle_shop_orders.csv")
    df.to_csv(f"{DBT_PROJECT_PATH}/data/raw_orders.csv")


@asset()
def raw_orders(extract_raw_orders):
    conn = create_raw_scheme()
    conn.execute(f'CREATE TABLE IF NOT EXISTS raw_orders AS SELECT * FROM "{DBT_PROJECT_PATH}/data/raw_orders.csv"')


@asset
def extract_raw_payments():
    os.makedirs(f"{DBT_PROJECT_PATH}/data", exist_ok=True)
    df = pd.read_csv("s3://dbt-tutorial-public/stripe_payments.csv")
    df.to_csv(f"{DBT_PROJECT_PATH}/data/raw_payments.csv")


@asset()
def raw_payments(extract_raw_payments):
    conn = create_raw_scheme()
    conn.execute(f'CREATE TABLE IF NOT EXISTS raw_payments AS SELECT * FROM "{DBT_PROJECT_PATH}/data/raw_payments.csv"')
