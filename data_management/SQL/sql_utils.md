# Group By
## Select Products that Appears More than One Time
``` sql
SELECT p.product_id
FROM `products` AS p
GROUP BY p.product_id
HAVING COUNT(*) > 1
LIMIT 1
```

# Record Repeated Type
## Filter for records with more than one entry
``` sql
SELECT id
FROM stores
WHERE ARRAY_LENGTH(products) > 1;
