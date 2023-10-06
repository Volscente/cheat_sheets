# General
## Clear
```sql
:clear
```

## Help
```sql
:help
```

# Call
## Show Database Graph
```sql
CALL db.schema.visualization()
```

# Match
## Return Distinct Values
```sql
# Template
MATCH (<variable_name>:<Node>)
RETURN <variable_name>
LIMIT 1

# Example
MATCH (g:Genre)
RETURN g
LIMIT 1 

# Output: Adventure
```