import os
from dagster import Definitions, file_relative_path
from dagster import load_assets_from_modules, load_assets_from_package_module
from dagster_dbt import load_assets_from_dbt_project, dbt_cli_resource
from dagster_dbt_jaffle.assets import raw_data

DBT_PROJECT_PATH = file_relative_path(__file__, "../../dbt_jaffle_shop")
DBT_PROFILES = file_relative_path(__file__, "../../dbt_jaffle_shop")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["jaffle_analytics"]
)

raw_data_assets = load_assets_from_package_module(
    raw_data,
    group_name="raw_data",
    key_prefix=["raw_data"],
)

resources = {
    "dbt": dbt_cli_resource.configured(
        {
            "project_dir": DBT_PROJECT_PATH,
            "profiles_dir": DBT_PROFILES,
        },
    ),
}

defs = Definitions(assets=[*dbt_assets, *raw_data_assets], resources=resources)