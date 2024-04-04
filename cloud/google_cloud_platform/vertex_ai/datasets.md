# Introduction
# Utils
## Create Dataset from BigQuery Table
- Create a BigQuery table in a BigQuery Dataset under the same location as your desired Vertex AI Dataset.
<details>
  <summary>Example Query</summary>
```sql
 /*
 Define the First Prototype input training dataset for Sales Predictor.
     Features: city, datetime information
     Label: average number of sales
 */
CREATE OR REPLACE TABLE `project_id.curated_dataset.training_dataset` AS
-- Retrieve sales in the selected time frame
WITH _sales_subset AS (
    SELECT
        *
    FROM
        `project_id.dim_dataset.sales`
    WHERE
        created_date BETWEEN DATE_SUB(@created_date_start_at, INTERVAL 1 DAY) AND @created_date_end_at
),
-- Retrieve active stores
_active_stores AS (
    SELECT
        *
    FROM
        `project_id.dim_dataset.stores`
),
-- Retrieve sales attributes for relevant sales
_relevant_sales_attributes AS (
    SELECT
        city,
        store_code,
        sale_code,
        DATE(created_at, timezone) AS created_date_local, -- Local timezone create date
        EXTRACT(HOUR FROM DATETIME(created_at, timezone)) AS hour_of_day,
        -- Bucketing into 15-minute intervals
        EXTRACT(MINUTE FROM TIMESTAMP_SECONDS((15*60) * DIV(UNIX_SECONDS(TIMESTAMP(DATETIME(created_at, timezone))), (15*60)))) AS minute_15_of_hour,
        -- Make the week start from Monday
        CASE EXTRACT(DAYOFWEEK FROM DATETIME(created_at, timezone))
            WHEN 1 THEN 7
            ELSE EXTRACT(DAYOFWEEK FROM DATETIME(created_at, timezone)) - 1
        END AS weekday,
    FROM
        _sales_subset
    WHERE
        -- Filter only for relevant sales
        is_test IS FALSE
        AND store_code NOT LIKE 'TEST_%' -- Removing test stores
),
-- Filter the order attributes only for stores
_relevant_store_sales_attributes AS (
    SELECT
        sales.store_code AS sales_store_code,
        stores.city,
        sales.order_code,
        sales.created_date_local,
        sales.weekday,
        sales.hour_of_day,
        sales.minute_15_of_hour
    FROM
        _relevant_sales_attributes AS sales
    INNER JOIN _active_stores AS stores
        ON sales.store_code = stores.store_code
        AND sales.city = sales.city
    WHERE
        stores.chain = 'BOOK' -- Filter for book stores
),
-- Compute number of sales group by datetime information
_number_of_sales_in_created_date AS (
    SELECT
        sales_store_code AS store_code,
        created_date_local,
        weekday,
        hour_of_day,
        minute_15_of_hour,
        COUNT(order_code) AS number_of_sales
    FROM
        _relevant_store_sales_attributes
    GROUP BY
        store_code,
        vendor_grade,
        created_date_local,
        weekday,
        hour_of_day,
        minute_15_of_hour
)
-- Compute the average number of orders per weekday, hour and 15-min bucket
SELECT
    store_code,
    weekday,
    hour_of_day,
    minute_15_of_hour,
    ROUND(AVG(number_of_sales), 0) AS average_number_of_sales
FROM
    _number_of_sales_in_created_date
WHERE
    store_code IN UNNEST(@store_codes)
GROUP BY
    store_code,
    weekday,
    hour_of_day,
    minute_15_of_hour
```

</details>
