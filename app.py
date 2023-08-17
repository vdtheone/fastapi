import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def index():
   return {"message": "mfdnf, World"}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

"""



import uvicorn
from fastapi import FastAPI, Path, Query, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []

# @app.post("/students/")
# async def student_data(s1: Student):
#    return s1


@app.post("/students")
async def student_data(name:str=Body(...),
marks:int=Body(...)):
   return {"name":name,"marks": marks}


@app.post("/students/{college}")
async def student_data(college:str, age:int, student:Student):
   retval={"college":college, "age":age, **student.model_dump()}
   return retval


@app.get("/")
async def index():
   return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}


@app.get("/profile/{id}")
async def profile(id:int):
   return {"id": id, "name": "vishal"}


@app.get("/hello/{name}/{age}")
async def greet(name:str,age:int):
   return {"name": name, "age":age} 


@app.get("/hello")
async def query_parameter(name:str,age:int):
   return {"name": name, "age":age}


@app.get("/helloo/{name}")
async def data(name:str,age:int):
   return {"name": name, "age":age}


@app.get("/{name}")
async def nameonly(name:str):
   return {"name": name}


@app.get("/validation/{name}")
async def hello_validation(name:str = Path(...,min_length=3, max_length=10)):
   return {"name": name}


@app.get("/validation/{name}/{age}")
async def validation(*, name: str=Path(...,min_length=3 , max_length=10), age: int = Path(..., ge=1, le=100)):
   return {"name": name, "age":age}


@app.get("/hello/{name}/{age}")
async def query_validation(*, name: str=Path(...,min_length=3 ,
max_length=10), \
      age: int = Path(..., ge=1, le=100), \
      percent:float=Query(..., ge=0, le=100)):
   return {"name": name, "age":age}  


@app.get("/temp/")
async def hello_template():
   ret='''
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
'''
   return HTMLResponse(content=ret)

# templates = Jinja2Templates(directory="templates")

@app.get("/hello/", response_class=HTMLResponse)
async def hello_template(request: Request):
   return templates.TemplateResponse("hello.html", {"request": request, "name": "vishal"})  


# app.mount(app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/name_img/{name}", response_class=HTMLResponse)
async def name_img(request: Request, name:str):
   return templates.TemplateResponse("hello.html", {"request": request, "name":name})




"""