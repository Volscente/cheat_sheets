# Common Errors
## Impossible to Import Module
```
poetry run pylint \
            --source-roots=./src \ # Add this
            --output-format=colorized \
            --msg-template='Rule: {msg_id} - Position: [{line},{column}] -  {msg}' \
            ./src ./tests
```
