# Import Standard Libraries
from fastapi import FastAPI
from enum import Enum

# Instantiate FastAPI
app = FastAPI()


class PackageSize(str, Enum):
    """
    Class that implements possible Package size
    """
    small = 'Small'
    medium = 'Medium'
    large = 'Large'


@app.get('/items/{item_id}')
async def get_item(item_id: int,
                   description: str | None = 'No Description'):
    """
    It takes a query parameters 'description' that is optional ( | None) and has a default value 'No Description'

    Args:
        item_id: Integer item id
        description: String item description

    Returns:
    """

    item = {'item_id': item_id}

    if description:

        item.update({'description': description})

    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int,
                         item_id: str,
                         q: str | None = None,
                         short: bool = False):
    """
    Use multiple path and query parameters

    Args:
        user_id: Integer user id
        item_id: String item id
        q: String query
        short: Boolean short flag

    Returns:
    """

    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get('/packages/{package_id}')
async def get_package(package_id: int,
                      size: PackageSize):
    """
    Retrieve package

    Args:
        package_id: Integer package id
        size: PackageSize enum required query parameter

    Returns:
    """

    return {'package_id': package_id,
            'size': size}
