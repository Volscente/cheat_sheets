# General
## Installation
```bash
brew install postgresql
```

## Extensions
```bash
# Vector Database
CREATE EXTENSION IF NOT EXISTS vector;

# Add vector column
ALTER TABLE your_table_name
ADD COLUMN embedding vector(768);
```

## Commands
### Service
```bash
# Start
brew services start postgresql@14

# Stop
brew services stop postgresql@14
```

### User
```bash
# Create user
createuser --interactive -P
```

### Database
```bash
# Create
createdb mydb

# Delete
dropdb mydb

# Access
psql mydb
```
