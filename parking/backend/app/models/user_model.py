from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    full_name = Column(String(100), index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    phone_num = Column(String(20), unique=True, nullable=False)
    state = Column(String(100), nullable=False)
    isAdmin = Column(Boolean, default=False)


