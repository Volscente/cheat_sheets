WITH src_listings AS (
    SELECT 
        *
    FROM
        {{ ref('src_listings') }} -- This is a reference to the model src_listings (Jinja syntax)
)