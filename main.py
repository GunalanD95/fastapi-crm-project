from fastapi import FastAPI 
from fastapi import APIRouter, Depends ,Request
from . import models
from .db import engine 
from .routers import user , lead ,login
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

models.Base.metadata.create_all(engine)

app = FastAPI()


BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

# importing the user router which we created in routers file
app.include_router(user.router) 
app.include_router(lead.router) 
app.include_router(login.router) 

@app.get("/", status_code=200)
def root(request: Request) -> dict:  # 2
    """
    Root GET
    """
    
    # 3
    return TEMPLATES.TemplateResponse(
        "login.html",
        {"request": request},
    )
