
import uvicorn
from fastapi import Cookie, FastAPI, Path, Query, Body, Request, Form, File, UploadFile, Header
import shutil
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field
app = FastAPI()


class supplier(BaseModel):
   supplierID:int
   supplierName:str

class product(BaseModel):
   productID:int
   prodname:str
   price:int
   supp:supplier

class customer(BaseModel):
   custID:int
   custname:str
   prod:Tuple[product]


@app.post('/invoice')
async def getInvoice(c1:customer):
   return c1





