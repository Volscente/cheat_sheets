# Import Standard Libraries
from fastapi import FastAPI
from enum import Enum


class Animal(str, Enum):
    """
    Define a class holding possible values for the 'animal' path parameter. No other values would be accepted.
    The class Animal inherits both from str and Enum.
    """

    cat = 'Cat'
    dog = 'Dog'
    bird = 'Bird'


# Instantiate FastAPI
app = FastAPI()


@app.get('/animals/{animal}')
async def get_animal(animal: Animal):
    """
    It accepts a path parameter 'animal' that comes from an Animal str enum class of possible values (Cat, Dog and Bird)

    Args:
        animal: Animal string enum of animals

    Returns:
        Dict animal string and message string
    """
    return {'animal': animal, 'message': 'You are looking for a {}'.format(animal)}


@app.get('/files/{file_path:path}')
async def get_files(file_path: str):

    return {'file_path': file_path}
