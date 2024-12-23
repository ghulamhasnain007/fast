# from sqlalchemy.orm import Session
# from app.models.user_model import User
# from app.schemas.user_schema import UserCreate
# from app.utils.hash_util import hash_password

# async def create_user(db: Session, user: UserCreate):
#     hashed_password =await hash_password(user.password)
#     db_user = User(
#         full_name=user.full_name,
#         email=user.email,
#         password=hashed_password,
#         phone_num=user.phone_num,
#         state=user.state,
#         isAdmin=False
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.utils.hash_util import hash_password

import logging

async def create_user(db: Session, user: UserCreate):
    try:
        if not hasattr(user, 'password'):
            raise ValueError("The 'user' object is missing the 'password' attribute.")
    
        print(f"User: {user}, Type: {type(user)}")
        print(f"DB: {db}, Type: {type(db)}")
        hashed_password = await hash_password(user.password)
        if(hashed_password):
            print(f"Password Hashed: {hashed_password}")
        db_user = User(
            full_name=user.full_name,
            email=user.email,
            password=hashed_password,
            phone_num=user.phone_num,
            state=user.state,
            isAdmin=False
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print(f"Error in create_user: {e}")
        raise e

