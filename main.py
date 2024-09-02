from typing import List
from uuid import UUID
from fastapi import FastAPI

from models import Gender, Role, User 

app = FastAPI()

db: List[User] = [
    User(
        id = UUID("3165d313-c956-477b-b9f6-33fb0520c8b8"), 
        first_name = "Jamila", 
        last_name = "Ahmed", 
        gender = Gender.female, 
        roles = [Role.student]
         ),
    User(
        id = UUID("42cfd3c7-5be4-4a27-afaf-16712a332b81"), 
        first_name = "Alex", 
        last_name = "Jones", 
        gender = Gender.male, 
        roles = [Role.admin, Role.user]
         )
]

@app.get("/")
async def root():
    return {"Hello": "Balls"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}