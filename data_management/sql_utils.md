# Group By
## Select Products that Appears More than One Time
```` sql
SELECT p.product_id
FROM `products` AS p
GROUP BY p.product_id
HAVING COUNT(*) > 1
LIMIT 1
