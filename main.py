from fastapi import FastAPI, File, UploadFile
from fastapi.param_functions import Form
from starlette.routing import Host
import uvicorn
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi.responses import FileResponse
import pandas as pd
import os

app = FastAPI()
templates = Jinja2Templates(directory="./static/templates")
app.mount('/static', StaticFiles(directory="./static"), name="static")


# @app.post("/user")
# async def main_page(request: Request,
#                 username: str = Form(...),
#                 password: str = Form(...)):
#     print("username: ", username)
#     print("password: ", password)
#     return templates.TemplateResponse("index.html",
#                                       {"request": request,
#                                        "username": username})

@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/tool01")
async def tool01_page(request:Request):
    return templates.TemplateResponse("tool01.html",{"request":request})

@app.post("/tool01")
async def upload_files(request: Request, file: bytes = File(...)):
    if len(file) > 0:
        excel = pd.read_excel(file)
        with pd.ExcelWriter('file/temp01.xlsx') as writer:
            excel.to_excel(writer, index=False)

@app.get("/tool02")
async def tool01_page(request:Request):
    return templates.TemplateResponse("tool02.html",{"request":request})

@app.post("/tool02")
async def upload_files(request: Request, file: bytes = File(...)):
    if len(file) > 0:
        excel = pd.read_excel(file)
        with pd.ExcelWriter('file/temp01.xlsx') as writer:
            excel.to_excel(writer, index=False)

    return templates.TemplateResponse("tool01.html", {"request": request})

@app.get("/file/{filename}")
async def download_tool01(request:Request,filename:str):
    file_path="./file/"+filename
    return FileResponse(file_path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)
