from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , db
from .. import models
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session


get_db = db.get_db
# Creating a user
def create_user(request,db : Session = Depends(get_db)):
    new_user = models.User(email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

