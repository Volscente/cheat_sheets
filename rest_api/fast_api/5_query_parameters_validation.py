# Import Standard Libraries
from fastapi import FastAPI, Query

# Instantiate FastAPI
# app = FastAPI()


# Define GET method with a validation on Query Parameter 'description' to not exceed 50 characters
@app.get('/items/{item_id}')
async def get_items(item_id: int,
                    description: str | None = Query(default=None, max_length=50)):

    # Define the Response Body
    response_body = {'item_id': item_id}

    if description:

        response_body.update()