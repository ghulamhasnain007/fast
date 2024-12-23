from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: int

# class UserBase(BaseModel):
#     id: int
#     full_name: str
#     email: str
#     password: str
#     phone_num: int
#     state: str
#     isAdmin: bool


class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True

# class UserCreate(UserBase):
#     pass

# class UserResponse(UserBase):
#     id: int

#     class Config:
#         orm_mode = True



class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    phone_num: str
    state: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone_num: str
    state: str
    # isAdmin: bool

    class Config:
        orm_mode = True