from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)



# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer(100), primary_key=True, autoincrement=True, index=True)
#     full_name = Column(String(100), index=True)
#     email = Column(String(255), unique=True, nullable=False)
#     password = Column(String(100), nullable=False)
#     phone_num = Column(Integer(20), unique=True, nullable=False)
#     state = Column(String(100), nullable=False)
#     isAdmin = Column(bool, default=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String(100), index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    phone_num = Column(String(20), unique=True, nullable=False)
    state = Column(String(100), nullable=False)
    # isAdmin = Column(bool, default=False)

