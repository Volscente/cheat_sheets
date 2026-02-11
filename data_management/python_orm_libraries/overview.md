# Introduction

## Components

The main components are:

- **Schema** (Pydantic model) &rarr; It validates incoming requests and outgoing responses (Data Validator)
- **Object-Relational Mapping - ORM** (SQLAlchemy Model) &rarr; Establish the database table structure
- **Service** - FastAPI

# Pydantic Model (Schema)

## Overview

The Pydantic model serves to:

- **Define Data Structure**: Outline the expected structure of the request body.
- **Validate Incoming Data**: Ensure that the data received adheres to the specified types and constraints.
- **Shape Response Data**: Optionally filter and format data before sending a response.

## Example

```python
# Pydantic model for a post request
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# Post request using the Pydantic model
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    pass
```

# SQLAlchemy Model (ORM)

## Overview

The SQLAlchemy model is dedicated to defining the database table structure. It includes:

- **Column Definitions**: Attributes such as post ID, title, content, published status, and creation timestamps.
- **Database Interaction Methods**: Functions to query, create, delete, and update database entries.

The SQLAlchemy model is defined in the `models.py` file.

## Model Creation

```python
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship, backref
from datetime import datetime

# Instance the base object
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    slug = Column(String(100), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content = Column(Text)
    author_id = Column(Integer(), ForeignKey('authors.id'))

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(255), nullable=False)
    joined = Column(DateTime(), default=datetime.now)

    # Reference external table
    articles = relationship('Article', backref='author')
```

The `authors` table is now defined, backreferencing the `author` column in the `Article` class. This creates a new column called author in the articles table. This column should contain the object of the user you define in the ORM.

## DB Creation

```python
# pip install sqlalchemy psycopg2

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Establish DB Connection
url = URL.create(
    drivername="postgresql",
    username="coderpad",
    host="/tmp/postgresql/socket",
    database="coderpad"
)
engine = create_engine(url)
connection = engine.connect()

# Define the two above mentioned mapped tables Articles and Authors

# Create the tables
Base.metadata.create_all(engine)
```

## Interact with Data

```python
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a couple some authors
ezz = Author(
    firstname="Ezzeddin",
    lastname="Abdullah",
    email="ezz_email@gmail.com"
)
ahmed = Author(
    firstname="Ahmed",
    lastname="Mohammed",
    email="ahmed_email@gmail.com"
)

# Create an article
article1 = Article(
    slug="clean-python",
    title="How to Write Clean Python",
    content="Lorem ipsum",
    author=ezz
    )

# Option 1: Add + Commit
session.add(article1)
session.commit()

# Option 2: Add All + Commit
session.add_all([article1, article2, article3])
session.commit()

# Option 3: Multipl Add + Flush + Commit
session.add(article2)
session.add(article3)
session.flush()
session.commit()
```

The session object registers transaction operations with `session.add()`, but doesn't yet communicate them to the database until `session.flush()` is called.

`session.flush()` communicates a series of operations to the database (insert, update, delete). The database maintains them as pending operations in a transaction. The changes aren't persisted permanently to disk, or visible to other transactions until the database receives a COMMIT for the current transaction (which is what `session.commit()` does).

`session.commit()` commits (persists) those changes to the database.

`flush()` is always called as part of a call to `commit()`.

## Query & Update Data

```python
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query Article table
article_query = session.query(Article)
clean_py_article = article_query.filter(Article.slug == "clean-python").first()

# Update
clean_py_query.update({Article.title: "Cleaner Python"})
```
