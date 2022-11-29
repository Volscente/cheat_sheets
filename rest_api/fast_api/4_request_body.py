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


# Define the POST methods
@app.post('/items')
async def post_item(item: Item):

    pass

