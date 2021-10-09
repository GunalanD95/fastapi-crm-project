from fastapi import APIRouter, Depends ,Request
from fastapi import FastAPI , status , Response , HTTPException
from fastapi.responses import HTMLResponse
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from ..repos import login
from fastapi.templating import Jinja2Templates
import os

# some of codes here....

# BASE_PATH = Path(__file__).parent.resolve()
# # lets say your template directory is under the root directory
# templates = Jinja2Templates(directory=f'{BASE_PATH}/templates')

router = APIRouter(
    tags=['login'],
    prefix="/login",
)
# operating_directory = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory="templates")
# templates = Jinja2Templates(directory=os.path.join(operating_directory, 'templates'))
#templates = Jinja2Templates(directory=os.path.dirname(os.path.abspath(__file__)))

#domain_template_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

            
@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html",{"request": request})
    #return templates.TemplateResponse(os.path.join(domain_template_directory, "login.html"), context={"request": request})


