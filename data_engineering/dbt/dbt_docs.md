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
#### Definition
It defines how models are stored and managed within the DWH. It is related to the *Core Layer* in the Data Flow. There are four different types of Materialisation:
- **View** - It is the default one and the model is represented as a View. It's good when you don't read the data too often, because the view is executed everytime.
- **Table** - The model is saved as a table and, everytime the DBT flow run, the table is re-created. It's good when you read the data often.
- **Incremental** - It is based on *Fact Tables* and it is used when you do not want to update the historical records. It appends data to a table.
- **Ephemeral** - It does not create anything in the DWH. It is used to exclude some views or tables from the final ones.

#### Configuration
In order to specify the default materialisation type among the above ones, go to the `dbt_project.yml` file and add the following lines:
```yml
models:
  dbtlearn:
    +materialized: view # Default materialisation type is 'view'
    dim:
        +materialized: table # Models inside 'models/dim' folder are materialized as 'table'
```
**NOTE:** Don't forget to execute `dbt run` after such changes.

#### View Materialisation
It can be set in the `dbt_project.yml` as the default one through:
```yml
models:
  dbtlearn:
    +materialized: view
```
or it can be set in the model definition by adding at the top:
```sql
{{
    config(
        materialized = 'view'
    )
}}
```

#### Table Materialisation
In order to create a  materialisation, create the corresponding model under the `models/dim` folder. Afterwards, run the command `dbt run`.

#### Incremental Materialisation
If you want to have an incremental materialisation, create the model under the `models/fct` folder and add the following configuration at the top:
```sql
{{
    config(
        materialized = 'incremental',
        on_schema_change='fail' -- What happen if the schema chages
    )
}}
```
It is also required to specify how DBT has to increment the table through a Jinga if statement like:
```sql
{% if is_incremental() %} -- If this is an incremental load (i.e. not creating table)
    AND review_date > (select max(review_date) from {{ this }}) -- Append this condition for incremental records
{% endif %}
```

Once a new record is inserted into the *Raw Layer*, it is possible to increment the materialised model by executing `dbt run`. To re-create the incremental materialization table from zero, use: `dbt run --full-refresh`.

#### Ephemeral Materialisation
Set the models you want to be ephemeral (a.k.a. excluded from the final tables) in the `dbt_project.yml`. For example every models inside the `src` folder:
```yaml
models:
  dbtlearn:
    +materialized: view
    dim:
      +materialized: table
    src:
      +materialized: ephemeral
```
In this way, when running `dbt run`, the models inside `src` folder won't be created. They become CTEs.
### Sources and Seeds
#### Sources
They are data already inside the DWH.
#### Seeds
They are data that are not inside the DWH. The *Seed* is the source of such data (e.g. Your local laptop).
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