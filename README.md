# trusted-data-pipeline


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
```