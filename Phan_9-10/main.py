from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()

task=[]

class Item(BaseModel):
    inputJob: str
    inputDate: str
    operation:str

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.get("/task")
async def get_task():
    return task

@app.post("/button_add")
async def add_task(item: Item):
    task.append({
        "job": item.inputJob,
        "date": item.inputDate,
    })
    return task

@app.delete("/button_delete")
async def delete_task(item: Item):
    task.remove({
        "job": item.inputJob,
        "date": item.inputDate,
    })
    return task
