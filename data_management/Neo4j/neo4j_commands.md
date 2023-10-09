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
## Return Anything
```sql
MATCH(anything) 
RETURN anything
LIMIT 5
```

## Return Distinct Values
```sql
-- Template
MATCH (<variable>:<Node>)
RETURN <variable>
LIMIT 1

-- Example
MATCH (g:Genre)
RETURN g
LIMIT 1 

-- Output: Node 'Genre'

-- Return the names
MATCH (g.Genre)
RETURN g.name

-- Output: ['Adventure', 'Animation', ...]
```

## Where Clause
```sql
-- Template
MATCH (<variable_1>:<Node_1>)-[:<relationship>]->(<variable_2>:<Node_2>)
WHERE <variable_2>.<property> = '<value>'
RETURN <varible_1>.<property>

-- Example
MATCH (m:Movie)-[:IN_GENRE]->(g:Genre)
WHERE g.name = 'Comedy'
RETURN m.title
```

## Return Multiple Nodes
```sql
-- Example
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)
WHERE m.title = 'What We Do in the Shadows'
RETURN actor, m
```

## Implicit Where Clause
```sql
/* 
    Return all the movies that have a relationship with the Person
    'Taika Waititi'
*/
MATCH(p:Person{name: 'Taika Waititi'})->(m:Movie)
RETURN p, m
```
**NOTE:** In the above example, the relationship is not specified. So, if there are multiple relationships between Person and Movie, it will return all of them (`ACTED_IN`, `DIRECTED`)

## Double Relationship
```sql
MATCH(:Person{name: 'Taika Waititi'})-[:ACTED_IN]->(m:Movie)<-[r:RATED]-(u:User)
RETURN m.title, properties(r)

/*
m.title: 'Boy'
properties(r): {
    'rating': 4.5
    'timestamp': 1386885137
}
*/
```

## OR Relationship
```sql
MATCH(person:Person)-[relation:ACTED_IN | DIRECTED]->(movie:Movie)
RETURN person, relation, movie
LIMIT 10
```

# Aggregations
## Average
```sql
MATCH(:Person{name: 'Taika Waititi'})-[:ACTED_IN]->(m:Movie)<-[r:RATED]-(u:User)
RETURN m.title AS Movie, avg(r.rating) AS AverageRating

/*
Movie: 'Boy'
AverageRating: 4.75
*/
```