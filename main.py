from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
fake_user_db = list()


class User(BaseModel):
    email: str
    pwd: str


@app.get("/users")
def get_users():
    return fake_user_db


@app.post("/register")
def create_user(user: User):
    fake_user_db.append({"id": user.email, "pwd": user.pwd})
    return {"message": "register success"}
