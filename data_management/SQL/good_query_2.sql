/*
 Vendor Profile includes several vendor-related characteristics for active, non-zombie, non-dormant and non-test
 vendor. In addition, it takes into account only selected entities, vertical types and transmission flows
 */
CREATE OR REPLACE TABLE `project_id.dataset.new_table_name` AS
-- Retrieve reporting entities
WITH _reporting_entities AS (
    SELECT *
    FROM
        `project_id.dataset.entities`
),

-- Retrieve vendors
_vendors AS (
    SELECT *
    FROM
        `project_id.dataset.vendors`
),

-- Retrieve vendor attributes
_vendor_attributes AS (
    SELECT
        attributes.*,
        vendor_code,
        entity_id,
        city_name,
        cuisine_name,
        is_active,
        is_test_vendor,
        orders_transmission_flow,
        key_account_sub_category
    FROM
        _vendors
),

-- Retrieve reporting entities vendor attributes
_reporting_entities_vendor_attributes AS (
    SELECT
        vendor_attributes.*,
        vendor_attributes.entity_id AS vendor_entity_id,
        entities.region,
        entities.country_code,
        entities.display_name
    FROM
        _vendor_attributes AS vendor_attributes
    INNER JOIN _reporting_entities AS entities
        ON vendor_attributes.entity_id = entities.entity_id
)

-- Apply filters for active restaurant vendors to build the Vendor Profile
SELECT
    region,
    country_code,
    display_name,
    city_name,
    vendor_entity_id AS entity_id,
    vendor_code,
    fixed_vendor_grade AS vendor_grade,
    vertical_type,
    vertical_food,
    cuisine_name,
    key_account_sub_category,
    successful_orders
FROM
    _reporting_entities_vendor_attributes
WHERE
    -- Filter all non-active, zombie, dormant and test vendors
    is_latest_record
    AND is_active
    AND NOT fixed_is_zombie_vendor
    AND NOT is_new_vendor
    AND NOT is_dormant_vendor
    AND NOT is_inoperative_vendor
    AND NOT is_test_vendor
    -- Filter for relevant vertical types
    AND vertical_type IN ('coffee', 'restaurants', 'street_food', 'home_based_kitchen')
    AND orders_transmission_flow = 'Restaurant' -- Exclude Logistic Service and Grocery
