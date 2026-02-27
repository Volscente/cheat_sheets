# SQLAlchemy ORM with Pydantic

## Create vs. Update

The below code shows the correct way to create a new ORM object in SQLAlchemy through Pydantic and how to update it.

```python
# Creation
db_word = models.Word(**word.model_dump())

# Update
update_data = word_update.model_dump(exclude_unset=True)
for key, value in update_data.items():
    setattr(db_word, key, value)
```

In the Creation case, the whole Pydantic object `word` is dumped into the SQLAlchemy ORM object `models.Word`. 
It includes also the default values in order to produce a complete ORM representation.
The reason why is not used for updating, is that, if a value is not provided in `word`, it would be overwritten with the
default value.

In the Update case, it only dumps the field set in `word_update`, without the non-set ones (`exclude_unset=True`).
This is used to prevent overwriting unset fields in the database.
After dumping the `word_update` into an SQLAlchemy ORM object `update_data`, only the non-unset fields are saved into the database
through the `db_word` SQLAlchemy ORM object
