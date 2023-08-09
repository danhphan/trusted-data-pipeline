# trusted-data-pipeline

This project is used as a demo for my talk: [Building 3D Trusted Data Pipelines With Dagster, Dbt, and Duckdb](https://2023.pycon.org.au/program/RY9ZCY/) at PyCon AU 2023

*Data pipelines and architecture*

<center><img src="./assets/image/3D_data_pipeline.png"/></center>


*Dagster global assets*

<center><img src="./assets/image/dagster_assets.png"/></center>

### Setup environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### DBT setup

```
cd ./dbt/jaffle_shop/
dbt deps
dbt build
dbt run
dbt test

dbt docs generate
dbt docs serve --port 8081

dbt show --inline "select count(*) from {{ ref('stg_customers') }}"
```