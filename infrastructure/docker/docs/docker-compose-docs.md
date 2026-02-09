## Volumes
### Definition

The `postgres_data` (Left side): This is the Named Volume. It’s managed by Docker. 
You don't usually see it in your project folder; it’s hidden in Docker's internal storage on your Mac/PC to ensure high performance.

The `/var/lib/postgresql/data` (Right side): This is the path inside the container where Postgres stores the actual database files.

Why the `volumes`: at the bottom? This is the "Declaration" section. It tells Docker: 
"I want to create a global storage unit named postgres_data that stays alive even if I stop the containers."

```Dockerfile
services:
  db:
    image: postgres:15-alpine
    container_name: vademecum_db
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build:
      context: .
      dockerfile: backend/Dockerfile
    container_name: vademecum_backend
    environment:
      # We construct the URL using the variables from .env
      DATABASE_URL: postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:
```
