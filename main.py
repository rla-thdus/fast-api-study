from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal

import crud
import schema

app = FastAPI()
fake_user_db = list()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", response_model=list[schema.User])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.post("/user", response_model=schema.User)
def create_user(user: schema.UserBase, db: Session = Depends(get_db)):
    db_user = crud.check_duplicated_email(db, user.email)
    if db_user:
        raise HTTPException(400, detail="email duplicated")
    user = crud.register_user(db, user)
    return user
