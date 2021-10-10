from fastapi import APIRouter, Depends
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from ..repos import lead

router = APIRouter(
    tags=['leads'],
    prefix="/lead", # initializing /lead as root page 
)

get_db = db.get_db # importing the db connection


# Creating a lead
@router.post('/create_lead') # we are using response model to limit the respone body which we want to show using schema class
def create_lead(request: schemas.Lead,db : Session = Depends(get_db)):
    return lead.create_lead(request,db)

@router.get('/get_all_leads')
def get_all_leads(response: Response,db: Session = Depends(get_db)):
    return lead.get_all_leads(db)


@router.get('/{id}')
def get_lead_id(id:int,response: Response, db: Session = Depends(get_db)):
    return lead.get_lead_by_id(id,db)

