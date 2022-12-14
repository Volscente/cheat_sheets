# Import Standard Libraries
from fastapi import FastAPI, Body
from pydantic import BaseModel


class Item(BaseModel):
    """
    Request body parameter defined through Pydantic
    """

    id: int
    price: float
    description: str | None = None


class User(BaseModel):
    """
    Request body parameter defined through Pydantic
    """

    user_id: int
    name: str
    age: int | None = None


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


# Multiple Request Body parameters
# NOTE: In case you want to add another Request Body parameter without defining its Pydantic model, use the Body() object
@app.post('/item_and_user/')
async def create_item_and_user(item: Item,
                               user: User,
                               importance: int | None = Body()):

    # Define the Response Body
    response_body = {'item_id': item.id,
                     'user_id': user.user_id}

    if importance:

        response_body.update({'importance': importance})

    return response_body
