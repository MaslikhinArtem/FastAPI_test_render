from typing import Annotated, Optional

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel

class Tasks(BaseModel):
    title: str
    body: str
    author: Optional[str] = None

class TaskAdd(Tasks):
    id: int

app = FastAPI(title='GuestRelation')

@app.get('/')
def index():
    return 'main page'

@app.post('/newtask')
async def add_task(task: Annotated[TaskAdd, Depends()]):
    return {'ok', True}


users = [
         {"id": 1, "author": "Jack", "title": "no"},
         {"id": 2, "author": "Jack", "title": "no"},
         {"id": 3, "author": "Jack", "title": "no"},
         {"id": 4, "author": "Jack", "title": "no"},
         {"id": 5, "author": "Jack", "title": "no"},
         {"id": 6, "author": "Jack", "title": "no"}
         ]


@app.post("/user/{user_id}")
async def user(user_id: int):
    return [i for i in users if user_id == i["id"]]





