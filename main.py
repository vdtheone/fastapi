
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


@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})


@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
   with open("destination.txt", "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
   return {"filename": file.filename}


@app.post("/cookie/")
def create_cookie():
   content = {"message": "cookie set"}
   response = JSONResponse(content=content)
   response.set_cookie(key="username", value="admin")
   return response


@app.get("/readcookie/")
async def read_cookie(username: str = Cookie(None)):
   return {"username": username}


@app.get("/headers/")
async def read_header(accept_language: Optional[str] = Header(None)):
   return {"Accept-Language": accept_language} 


@app.get("/rspheader/")
def set_rsp_headers():
   content = {"message": "Hello World"}
   headers = {"X-Web-Framework": "FastAPI", "Content-Language": "en-US"}
   return JSONResponse(content=content, headers=headers)








