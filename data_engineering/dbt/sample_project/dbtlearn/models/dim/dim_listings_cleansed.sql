WITH src_listings AS (
    SELECT 
        *
    FROM
        {{ ref('src_listings') }} -- This is a reference to the model src_listings (Jinja syntax)
)
SELECT
    listing_id,
    listing_name,
    room_type,
    CASE
        WHEN minimum_nights = 0 THEN 1
        ELSE minimum_nights
    END AS minimum_nights,
    host_id,
    REPLACE(
        price_str,
        '$' -- Replace the dollar sign with nothing
    ) :: NUMBER( -- Convert through "::" operator the string to a number of 2 decimal places
        10,
        2
    ) AS price,
    created_at,
    updated_at
FROM
 src_listings