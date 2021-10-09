from fastapi import FastAPI 
from fastapi import APIRouter, Depends ,Request
from . import models
from .db import engine 
from .routers import user , lead ,login
from fastapi.templating import Jinja2Templates
import os
from fastapi.staticfiles import StaticFiles
from pathlib import Path


models.Base.metadata.create_all(engine)

app = FastAPI()

# importing the user router which we created in routers file
app.include_router(user.router) 
app.include_router(lead.router) 
app.include_router(login.router) 

BASE_PATH = Path(__file__).resolve().parent
app.mount(
    "/static",
    StaticFiles(directory=BASE_PATH/ "static"),
    name="static",
)

