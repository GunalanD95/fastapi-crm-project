from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base

class User(Base):
    __tablename__ ="users"

    id =Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)