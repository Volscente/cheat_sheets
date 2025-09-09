# General
## Installation
```bash
brew install postgresql
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
