from fastapi import APIRouter, Depends ,Request
from fastapi import FastAPI , status , Response , HTTPException, Form
from fastapi.responses import HTMLResponse
from .. import schemas , models , db
from ..db import engine ,SessionLocal,BASE_PATH
from sqlalchemy.orm import Session
from ..repos import login
from ..repos .login import Login
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path
from fastapi.encoders import jsonable_encoder

get_db = db.get_db
router = APIRouter(
    tags=['login'],
    prefix="/login",
)
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

            
@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return TEMPLATES.TemplateResponse("login.html",{"request": request})


@router.post("/")
async def ps_login(request: Request,db: Session = Depends(get_db)):
    form_data = await request.form()
    da = jsonable_encoder(form_data)
    print(form_data,"dfnkfn")
    print(form_data['email'],"gotitt")
    email = form_data['email']
    pwd = form_data['password']
    lead = db.query(models.User).filter(models.User.email== email).first()
    if lead:
        password = db.query(models.User).filter(lead.password== pwd).first() 
        if password:     
            return "Login Success"
    else:
        return "invalid user"