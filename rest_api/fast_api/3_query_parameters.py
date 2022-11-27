# Import Standard Libraries
from fastapi import FastAPI

# Instantiate FastAPI
app = FastAPI()


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

    if description:

        return {'item_id': item_id, 'description': description}

    else:

        return {'item_id': item_id}
