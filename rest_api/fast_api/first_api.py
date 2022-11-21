# Import Standard Libraries
from fastapi import FastAPI

# Instantiate FastAPI
service = FastAPI()


@service.get("/")
async def root():
    return {"message": "Hello World"}

