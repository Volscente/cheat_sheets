# Import Standard Libraries
from fastapi import FastAPI, Query, Path

# Instantiate FastAPI
app = FastAPI()


# Define GET method with a validation on Optional Query Parameter 'description' between 3 and 50 characters and starting with 'C'
@app.get('/items/{item_id}')
async def get_items(item_id: int,
                    description: str | None = Query(default=None, # You can pass whatever default value, also a String
                                                    min_length=3,
                                                    max_length=50,
                                                    regex="^C")):

    # Define the Response Body
    response_body = {'item_id': item_id}

    if description:

        response_body.update({'description': description})

    return response_body


# Define the Required Query Parameter that should start with a capital letter and be at least 2 characters
@app.get('/users/')
async def get_users(name: str = Query(min_length=2, # You can also specify the mandatory field as 'default=...'
                                      regex="^[A-Z]")):

    # Define the response body
    response_body = {'name': name}

    return response_body


# Define a Query Parameter of type List
@app.get('/user_list/')
async def get_user_list(users: list[str] | None = Query(default=['john', 'sam'])):

    return {'users': users}


# It is possible to define the same Data Validation on a Path Parameter
# NOTE: Path and Query Data Validation can contain a 'title' element
@app.get('/orders/{order_id}')
async def get_orders(order_id: str = Path(title='The ID of the order',
                                          min_length=3,
                                          max_length=3),
                     description: str | None = Query(default=None,
                                                     title='The order description',
                                                     max_length=20)):

    response_body = {'order_id': order_id}

    if description:

        response_body.update({'description': description})

    return response_body


# Numeric validation
@app.get('/orders/')
async def get_orders(number_orders: int = Query(default=0, ge=0, le=10)):

    return {'number_orders': number_orders}
