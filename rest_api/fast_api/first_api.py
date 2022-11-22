# Import Standard Libraries
from fastapi import FastAPI

# Instantiate FastAPI
service = FastAPI()


@service.get("/")
async def root():
    return {"message": "Hello World"}

@service.get('/items/{item_id}')
async def get_item(item_id: str):

    return {'item': item_id}