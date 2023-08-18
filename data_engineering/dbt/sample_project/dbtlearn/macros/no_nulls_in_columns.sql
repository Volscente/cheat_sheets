-- It will check if there are nulls in the columns of the given model
{% macro no_nulls_in_columns(model) %}
    SELECT 
        * 
    FROM
         {{ model }} 
    WHERE
        {% for col in adapter.get_columns_in_relation(model) -%}
            {{ col.column }} IS NULL OR
        {% endfor %}
        FALSE -- This is to remove the last OR
{% endmacro %}s