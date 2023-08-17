
import uvicorn
from fastapi import Cookie, FastAPI, Path, Query, Body, Request, Form, File, UploadFile, Header
import shutil
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field
app = FastAPI()


data = []
class Book(BaseModel):
   id: int
   title: str
   author: str
   publisher: str


@app.post("/book")
def add_book(book: Book):
   data.append(book.model_dump())
   return data


@app.get("/list")
def get_books():
   return data


@app.get("/book/{id}")
def get_book(id: int):
   id = id - 1
   return data[id]


@app.put("/book/{id}")
def add_book(id: int, book: Book):
   data[id-1] = book
   return data


@app.delete("/book/{id}")
def delete_book(id: int):
   data.pop(id-1)
   return data





