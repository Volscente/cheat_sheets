# Import Standard Libraries
from pydantic import BaseModel


# Every class extends the BaseModel
class User(BaseModel):

    # The 'id' is required, because it has no default value
    id: int

    # The 'name' is optional, because it has a default value ('John Doe')
    # NOTE: the type is inferred from the default value, so the type annotation is optional
    name: str = 'John Doe'

    friend_ids: list[int] = []


# User 1
user_1_dict = {
    'id': '1',
    'friend_ids': [1, 2, '3']
}

user = User(**user_1_dict)

print('User ID')
print(type(user.id))
print(user.id)
print('')

print('User Name')
print(type(user.name))
print(user.name)
print('')

print('User Friend IDs')
print(type(user.friend_ids))
print(user.friend_ids)
print('')

# User 2
user_2_dict = {
    'id': 2,
    'name': 'Will',
    'friend_ids': [4, 5, 6]
}

user_2 = User(**user_2_dict)

print('User ID')
print(type(user_2.id))
print(user_2.id)
print('')

print('User Name')
print(type(user_2.name))
print(user_2.name)
print('')

print('User Friend IDs')
print(type(user_2.friend_ids))
print(user_2.friend_ids)
print('')

# User 3 - It will raise a ValidationError because the 'id' can not be forced to Integer
user_3_dict = {
    'id': '3.1',
    'friend_ids': []
}

user_3 = User(**user_3_dict)
