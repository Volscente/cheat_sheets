{% snapshot scd_raw_listings %} -- Snapshot Jinja tag with the name of the snapshot

{{
    config(
    target_schema='dev', -- Destination of the snapshot
    unique_key='id', -- Unique attribute to identify the rows
    strategy='timestamp',
    updated_at='updated_at', -- Attribute to identify the last update
    invalidate_hard_deletes=True)
}}

-- Define the data to be snapshotted
SELECT 
    * 
FROM 
    {{ source('airbnb', 'listings') }}

{% endsnapshot %}