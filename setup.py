from setuptools import find_packages, setup

setup(
    name="files-dbt-bigquery",
    version="0.1",
    description="Meltano project files for dbt-bigquery",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/models/.gitkeep",
            "transform/profiles/bigquery/profiles.yml",
            "transform/.gitignore",
            "transform/dbt_project.yml",
        ]
    },
)
