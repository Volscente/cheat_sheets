# Steps
## 1. Create User
- Create `TRANSFORM` role
```sql
-- Switch to admin role
USE ROLE ACCOUNTADMIN;

-- Create new role
CREATE ROLE IF NOT EXISTS TRANSFORM;

-- Add the new role to the admin role
GRANT ROLE TRANSFORM TO ROLE ACCOUNTADMIN;
```
- Create new user `dbt`
```sql
-- Create use 'dbt'
CREATE USER IF NOT EXISTS dbt
  PASSWORD='dbtPassword123'
  LOGIN_NAME='dbt'
  MUST_CHANGE_PASSWORD=FALSE
  DEFAULT_WAREHOUSE='<warehouse_name>' -- COMPUTE_WH
  DEFAULT_ROLE='<role_name>' -- TRANSFORM
  DEFAULT_NAMESPACE='<namespace>.RAW' -- AIRBNB.RAW
  COMMENT='DBT user used for data transformation';
```
- Create DWH
```sql
CREATE DATABASE IF NOT EXISTS <dwh_name> -- AIRBNB
```