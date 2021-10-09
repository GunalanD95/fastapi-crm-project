from fastapi import APIRouter, Depends ,Request
from fastapi import FastAPI , status , Response , HTTPException
from fastapi.responses import HTMLResponse
from .. import schemas , models , db
from ..db import engine ,SessionLocal,BASE_PATH
from sqlalchemy.orm import Session
from ..repos import login
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

router = APIRouter(
    tags=['login'],
    prefix="/login",
)
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

            
@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return TEMPLATES.TemplateResponse("index.html",{"request": request})


