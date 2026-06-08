from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    title: str
    description: str | None = None

users: List[User] = []
items: List[Item] = []

@app.get("/users", response_model=List[User])
def list_users():
    return users

@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    if any(existing.id == user.id for existing in users):
        raise HTTPException(status_code=400, detail="User ID already exists")
    users.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
