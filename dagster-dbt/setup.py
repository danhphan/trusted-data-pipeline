from setuptools import find_packages, setup

setup(
    name="dagster_dbt",
    packages=find_packages(exclude=["dagster_dbt_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
