from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
from models import User, Gender, Role
from uuid import UUID, uuid4

app=FastAPI()

db: List[User]=[
    User(
        id=uuid4(),
        first_name="Karthika",
        last_name="Vijay",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Radha",
        last_name="Vijay",
        gender=Gender.female,
        roles=[Role.student]
    )
]
@app.get("/api/users")
def users():
    return db