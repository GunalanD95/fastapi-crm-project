from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from ..repos import user

router = APIRouter(
    tags=['users'],
    prefix="/user", # initializing /user as root page 
)

get_db = db.get_db # importing the db connection


# Creating a user
@router.post('/create_user') # we are using response model to limit the respone body which we want to show using schema class
def create_user(request: schemas.User,db : Session = Depends(get_db)):
    return user.create_user(request,db)
