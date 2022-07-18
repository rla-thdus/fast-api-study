from sqlalchemy.orm import Session
from model import User
from schema import UserBase


def register_user(db: Session, user: UserBase):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user