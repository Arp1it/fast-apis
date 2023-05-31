# from typing import Union

# from fastapi import FastAPI

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://jaiswalrraa12:yFo8Eygmwbywhhgd@cluster0.ghhea35.mongodb.net")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs = conn.notes.notes.find_one({})
    # print(docs)

    docs = conn.notes.notes.find({})
    # for doc in docs:
    #     # print(doc)
    #     print(doc['_id'])

    # # print(docs)

    newDocs = []

    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })

    return templates.TemplateResponse("index.html", {"request": request, "newdocs": newDocs})


@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}