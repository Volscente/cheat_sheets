# Import Standard Libraries
from fastapi import FastAPI
from enum import Enum


class Animal(str, Enum):
    """
    Define a class holding possible values for the 'animal' path parameter. No other values would be accepted
    """

    cat = 'Cat'
    dog = 'Dog'
    bird = 'Bird'


# Instantiate FastAPI
app = FastAPI()


@app.get('/animals/{animal}')
async def get_animal(animal: Animal):

    match animal:
        case Animal.cat:
            return {'animal': animal, 'message': 'You are looking for a cat'}
        case Animal.dog:
            return {'animal': animal, 'message': 'You are looking for a dog'}
        case Animal.bird:
            return {'animal': animal, 'message': 'You are looking for a bird'}

