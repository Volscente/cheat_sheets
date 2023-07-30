# Role Management
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
# Warehouse Management
## Create Warehouse
```sql
-- Create new Warehouse 'COMPUTE_WH'
CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH;
```