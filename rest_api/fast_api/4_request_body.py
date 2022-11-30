# Import Standard Libraries
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    """
    Request body defined through Pydantic
    """

    id: int
    price: float
    description: str | None = None


# Instantiate FastAPI
app = FastAPI()


# Define POST method with Request Body
@app.post('/items')
async def insert_item(item: Item):

    return 'Inserted item: {}'.format(item.id)


# Define POST method with Request Body, Path Parameter and Optional Query Parameter
@app.post('/items/{item_id}')
async def create_item(item_id: int,
                      item: Item,
                      note: str | None = None):

    # Define the Response Body
    response_body = {'item_id': item_id,
                     'create_item_id': item.id}

    if note:
        response_body.update({'note': note})

    return response_body
