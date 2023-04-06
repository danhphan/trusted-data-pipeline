from setuptools import find_packages, setup

setup(
    name="dagster_dbt_jaffle",
    packages=find_packages(exclude=["dagster_dbt_jaffle_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
