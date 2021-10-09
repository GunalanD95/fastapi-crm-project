import re
from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , db
from .. import models
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session


get_db = db.get_db
# Creating a user
def create_lead(request,db : Session = Depends(get_db)):
    new_lead = models.Lead(lead_name=request.lead_name,cus_name=request.cus_name,lead_date=request.lead_date,lead_amount=request.lead_amount)
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead


def get_all_leads(db: Session):
    all_leads = db.query(models.Lead).all()
    return all_leads

def get_lead_by_id(id:int,db: Session):
    lead = db.query(models.Lead).filter(models.Lead.id== id).first()
    return lead