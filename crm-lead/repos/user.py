from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , db
from .. import models
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from typing import Optional


get_db = db.get_db
# Creating a user
def create_user(request,db : Session = Depends(get_db)):
    new_user = models.User(email=request.email,password=request.password,user_name=request.user_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#getting user with name

def get_user(id:int,response: Response,db : Session = Depends(get_db)):
    get_user = db.query(models.User).filter(models.User.id== id).first()
    return get_user

