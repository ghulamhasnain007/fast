# from fastapi import APIRouter
# from app.models.user_model import User
# from app.controllers.user_controller import create_user

# router = APIRouter()



# @router.post("/api/user/register/")
# async def add_user(user: User):
#     return await create_user(user)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse
from app.controllers.user_controller import create_user
from app.core.database import get_db

router = APIRouter()


@router.post("/api/user/register/")
async def add_user(user: UserCreate, db: Session = Depends(get_db)):
    print(f"User from routes: {user}, Type: {type(user)}")
    print(f"DB from routes: {db}, Type: {type(db)}")
    return await create_user(db, user)

