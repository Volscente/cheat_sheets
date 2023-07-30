# User
## Create User
```sql
-- Create use 'dbt'
CREATE USER IF NOT EXISTS dbt
  PASSWORD='dbtPassword123'
  LOGIN_NAME='dbt'
  MUST_CHANGE_PASSWORD=FALSE
  DEFAULT_WAREHOUSE='<warehouse_name>'
  DEFAULT_ROLE='<role_name>'
  DEFAULT_NAMESPACE='<namespace>.RAW'
  COMMENT='DBT user used for data transformation';
```
# Role
## Use Role
```sql
-- Use the role 'ACCOUNTADMIN'
USE ROLE ACCOUNTADMIN;
```
## Create Role
```sql
-- Create the role 'TRANSFORM'
CREATE ROLE IF NOT EXISTS TRANSFORM;
```
## Modify Role
```sql
-- Add the role 'TRANSFORM' to the role 'ACCOUNTADMIN'
GRANT ROLE TRANSFORM TO ROLE ACCOUNTADMIN;
```
## Add Permission to Role
```sql
-- Add the operate premission 'OPERATE' on the dwh 'COMPUTE_WH' to the role 'TRANSFORM'
GRANT OPERATE ON WAREHOUSE COMPUTE_WH TO ROLE TRANSFORM;
```
## Grant Role to User
```sql
-- Grant the role 'TRANSFORM' to user 'dbt'
GRANT ROLE TRANSFORM to USER dbt;
```
## List of Required Permissions
```sql
GRANT ALL ON WAREHOUSE COMPUTE_WH TO ROLE transform; 
GRANT ALL ON DATABASE AIRBNB to ROLE transform;
GRANT ALL ON ALL SCHEMAS IN DATABASE AIRBNB to ROLE transform;
GRANT ALL ON FUTURE SCHEMAS IN DATABASE AIRBNB to ROLE transform;
GRANT ALL ON ALL TABLES IN SCHEMA AIRBNB.RAW to ROLE transform;
GRANT ALL ON FUTURE TABLES IN SCHEMA AIRBNB.RAW to ROLE transform;
```
# Warehouse
## Create Warehouse
```sql
-- Create new Warehouse 'COMPUTE_WH'
CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH;
```
# Database 
## Create Database
```sql
-- Create new Database 'AIRBNB'
CREATE DATABASE IF NOT EXISTS AIRBNB;
```
## Create Schema
```sql
-- Create new Schema 'RAW' in Database 'AIRBNB'
CREATE SCHEMA IF NOT EXISTS AIRBNB.RAW;
```