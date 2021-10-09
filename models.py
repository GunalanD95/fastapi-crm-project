from sqlalchemy import Boolean, Column, ForeignKey, Integer, String ,DateTime,Float,Date
from sqlalchemy.orm import relationship
import datetime
from datetime import date

from .db import Base

class User(Base):
    __tablename__ ="users"

    id =Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    user_name = Column(String)


class Lead(Base):
    __tablename__ ="leads"

    id =Column(Integer, primary_key=True, index=True)
    lead_name = Column(String)
    cus_name = Column(String)
    lead_date = Column(Date,default=date.today())
    lead_amount = Column(Float)
