from fastapi import FastAPI 
from fastapi import APIRouter, Depends ,Request
from . import models
from .db import engine 
from .routers import user , lead ,login
from fastapi.templating import Jinja2Templates
import os

models.Base.metadata.create_all(engine)

app = FastAPI()



# importing the user router which we created in routers file
app.include_router(user.router) 
app.include_router(lead.router) 
app.include_router(login.router) 
