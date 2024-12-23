from sqlalchemy.orm import Session
from models import Item, User
from passlib.hash import bcrypt
# from models import User
from schemas import ItemCreate, UserCreate

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


from passlib.hash import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hash(password)

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        phone_num=user.phone_num,
        state=user.state,
        # isAdmin=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
