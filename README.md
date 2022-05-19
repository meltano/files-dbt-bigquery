# files-dbt-bigquery

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [dbt](https://www.getdbt.com/).

Files:
- [`transform/models`](./bundle/transform/models) (directory)
- [`transform/profiles/bigquery/profiles.yml`](./bundle/transform/profiles/bigquery/profiles.yml)
- [`transform/dbt_project.yml`](./bundle/transform/dbt_project.yml)
- [`transform/.gitignore`](./bundle/transform/.gitignore)

```py
# Add dbt-bigquery transformer and this file bundle to your Meltano project
meltano add transformer dbt-bigquery

# Add only this file bundle to your Meltano project
meltano add files dbt-bigquery
```
