from .db import Base
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime, time, timedelta


class User(BaseModel):
    email:str
    password:str
    user_name:str


class Lead(BaseModel):
    lead_name:str
    cus_name:str
    lead_date:date 
    lead_amount:float