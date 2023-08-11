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
## Components
### Models
They are the basic building blocks of DBT. They are materialized as tables or views and are located in the `models` folder as SQL files. They can also refer each other and use templates and macros.
#### Common Table Expression (CTE)
They are temporary named result and have a form like:
```sql
WITH <name_cte> (
    [column_names]
) AS 
(
    <cte_query>
)
```
Models created under the `models` folder can be structured in subfolders, refelecting the layer which they belong to (e.g., `src` for the Staging Layer, etc.).
Once a model is created, use the following command (`dbt run`) to create the corresponding view in the schema selected:
![DBT Overview](./../../images/data_engineering/dbt_3.png)
### Materialisation
It defines how models are stored and managed within the DWH. There are four different types of Materialisation:
- **View** - It is the default one and the model is represented as a View. It's good when you don't read the data too often.
- **Table** - The model is saved as a table and, everytime the DBT flow run, the table is re-created. It's good when you read the data often.
- **Incremental**
- **Ephemeral**
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
The command will create a `profile.yml` file inside the `~/.dbt` folder.
**NOTE 3:** In the file `<project_name>.yml` delete the example lines in the `models/<project_name>`
**NOTE 4:** Delete the example files under the `models` folder.
## Debug
```bash
# From inside the DBT Project, execute the command to check the connection
dbt debug
```