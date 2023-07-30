import os
from dagster import Definitions, load_assets_from_modules, file_relative_path
from dagster_dbt import load_assets_from_dbt_project, dbt_cli_resource


DBT_PROJECT_PATH = file_relative_path(__file__, "../../dbt_jaffle_shop")
DBT_PROFILES = file_relative_path(__file__, "../../dbt_jaffle_shop")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["jaffle_analytics"]
)

resources = {
    "dbt": dbt_cli_resource.configured(
        {
            "project_dir": DBT_PROJECT_PATH,
            "profiles_dir": DBT_PROFILES,
        },
    ),
}

defs = Definitions(assets=[*dbt_assets], resources=resources)