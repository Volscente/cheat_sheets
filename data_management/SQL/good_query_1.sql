/*
 Retrieve vendor schedules for selected reporting entities
 */
-- Retrieve reporting entities
WITH _entities AS (
    SELECT *
    FROM
        `project_id.dataset.entities`
),

-- Retrieve vendor schedules
_schedules AS (
    SELECT *
    FROM
        `project_id.dataset.schedules`
    WHERE
        metadata.type = 'vendor-schedule' -- Filter only for schedules
),

-- Filter schedules for reporting entities
_relevant_schedules AS (
    SELECT
        schedules.global_entity_id AS entity_id,
        schedules.content.vendor.id AS vendor_code,
        schedules.content.time_zone AS timezone,
        schedules.created_date,
        schedules.timestamp,
        schedules.content.schedules.*,
    FROM
        _schedules AS schedules
    INNER JOIN _entities AS entities
        ON
            schedules.global_entity_id = entities.entity_id
),

-- Retrieve latest schedule updates for each [entity, vendor] group
_latest_schedule_update_at AS (
    SELECT
        entity_id,
        vendor_code,
        MAX(timestamp) AS latest_update_at
    FROM
        _relevant_schedules
    GROUP BY
        entity_id,
        vendor_code
),

-- Retrieve the latest relevant schedules
_latest_relevant_schedules AS (
    SELECT
        schedules.entity_id,
        schedules.vendor_code,
        schedules.created_date,
        schedules.timestamp AS created_at,
        schedules.timezone,
        schedules.monday AS monday_schedule,
        schedules.tuesday AS tuesday_schedule,
        schedules.wednesday AS wednesday_schedule,
        schedules.thursday AS thursday_schedule,
        schedules.friday AS friday_schedule,
        schedules.saturday AS saturday_schedule,
        schedules.sunday AS sunday_schedule
    FROM
        _relevant_schedules AS schedules
    INNER JOIN _latest_schedule_update_at AS updates
        ON
            schedules.entity_id = updates.entity_id
            AND schedules.vendor_code = updates.vendor_code
            AND schedules.timestamp = updates.latest_update_at
    WHERE
        -- Exclude empty schedules
        (
            NOT TO_JSON_STRING(schedules.monday) LIKE '%null%'
            OR NOT TO_JSON_STRING(schedules.tuesday) LIKE '%null%'
            OR NOT TO_JSON_STRING(schedules.wednesday) LIKE '%null%'
            OR NOT TO_JSON_STRING(schedules.thursday) LIKE '%null%'
            OR NOT TO_JSON_STRING(schedules.friday) LIKE '%null%'
            OR NOT TO_JSON_STRING(schedules.saturday) LIKE '%null%'
            OR NOT TO_JSON_STRING(schedules.sunday) LIKE '%null%'
        )
)

SELECT
    DISTINCT entity_id
FROM
    _latest_relevant_schedules

