# Introduction
## Installation
```bash
pip install dbt-snowflake==1.5.0
```
## Configuration
You should have a `.dbt` in your home directory.
## Overview
Following the ELT principle, the data transformation happens inside the DWH through several steps that allows easily 
debugging the whole process.
![DBT Overview](./../../images/data_engineering/dbt_1.png)
# CLI
## Prompt
```bash
dbt
```
## Init Project
```bash
dbt init <project_name>
```
**NOTE:** You will need your user-organization information, you can find them in the bottom left corner of DBT (`DIQBEUO-PD08962`)
![DBT Information](./../../images/data_engineering/dbt_2.png)
**NOTE 2:** The username and password are the ones setup on the DWH, not of Snowflake!