from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    phone_num: str
    state: str
    isAdmin: bool

class UserResponse(BaseModel):
    pass
    # id: int
    # full_name: str
    # email: str
    # phone_num: str
    # state: str
    # isAdmin: bool

    class Config:
        orm_mode = True
