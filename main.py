from fastapi import FastAPI 
from . import models
from .db import engine 
from .routers import user

models.Base.metadata.create_all(engine)

app = FastAPI()


# importing the user router which we created in routers file
app.include_router(user.router) 


