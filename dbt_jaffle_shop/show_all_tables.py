import duckdb as db
import pandas as pd

conn = db.connect('jaffle_shop_db.duckdb')

table_df = conn.sql("SHOW ALL TABLES").df()

print(table_df[["database", "schema", "name", "temporary"]])