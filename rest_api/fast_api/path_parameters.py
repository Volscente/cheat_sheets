# Import Standard Libraries
from fastapi import FastAPI
from enum import Enum


class Animal(str, Enum):
    """
    Define a class holding possible values for the 'animal' path parameter
    """

    cat = 'Cat'
    dog = 'Dog'
    bird = 'Bird'


# Instantiate FastAPI
app = FastAPI()


@app.get('animals/{animal}')
async def get_animal(animal: Animal):

    pass

