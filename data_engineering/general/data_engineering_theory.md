# Data Management
## Data Characteristics (The 3 Vs)
- Variety - How different are data
- Velocity - How fast data should be ingested
- Volume - How much data
## Data Area Hierarchy
1. **Data Collection** - Extract data from several sources in different formats
2. **Data Wrangling** - Improve the data quality (clean data, handle missing values, address inconsistent data, etc.)
3. **Data Integration** - Load data into a sink destination
4. **BI and Analytics**
5. **Machine Learning**
## ETL vs ELT
The first three steps of the Data Area Hierarchy can be associated to the **ETL Process** (Extract, Transform and Load).
This approach was initially designed so that the transformation step takes place outside the database. That was due to
resource constraints.
However, right now the data storage resources are really powerful, and it is now preferable the **ELT Process**.
In here the transformations happen inside the database, since the computational power is so high that there is not the need
anymore to do the transformations elsewhere. 
# Data Warehouse (DWH)
## Purpose
It acts as the source of truth for Data Analytics and Data Reporting teams. They are not designed for unstructured data.
Here is the destination of an ETL/ELT process.
## Technologies
- AWS Redshift
- Google BigQuery
- Snowflake