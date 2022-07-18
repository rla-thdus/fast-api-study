from sqlalchemy.orm import Session
from schema import UserBase
import model


def register_user(db: Session, user: UserBase):
    db_user = model.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def check_duplicated_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()