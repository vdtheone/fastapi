
import uvicorn
from fastapi import Cookie, FastAPI, Path, Query, Body, Request, Form, File, UploadFile, Header
import shutil
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class User(BaseModel):
   username:str
   password:str

# @app.post("/submit/", response_model=User)
# async def submit(nm: str = Form(...), pwd: str = Form(...)):
#    return User(username=nm, password=pwd)


@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("login.html", {"request": request})


@app.post("/submit/")
async def submit(nm: str = Form(...), pwd: str = Form(...)):
   return {"username": nm, "password": pwd}


