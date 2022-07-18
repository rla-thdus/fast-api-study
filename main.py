from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from crud import register_user
from database import Base, engine, SessionLocal
from schema import UserBase

app = FastAPI()
fake_user_db = list()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users")
def get_users():
    return fake_user_db


@app.post("/register")
def create_user(user: UserBase, db: Session = Depends(get_db)):
    register_user(db, user)
    return {"message": "register success"}


