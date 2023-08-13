# trusted-data-pipeline

This project is used as a demo for my talk: [Building 3D Trusted Data Pipelines With Dagster, Dbt, and Duckdb](https://2023.pycon.org.au/program/RY9ZCY/) at PyCon Australia 2023

*Data pipelines and architecture*

<center><img src="./assets/image/3D_data_pipeline.png"/></center>


*Dagster global assets*

<center><img src="./assets/image/dagster_assets.png"/></center>

### Setup Python environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### Setup Dagster

```
cd ./dagster_dbt_jaffle/
dagster dev # or: dagit
```

### Setup Dbt

```
cd ./dbt_jaffle_shop/
dbt deps
dbt build
```

### Run and test Dbt models

```
dbt run
dbt test
dbt test --select customers
```

### Generate and view docs

```
dbt docs generate
dbt docs serve --port 8081

dbt show --inline "select count(*) from {{ ref('stg_customers') }}"
```

