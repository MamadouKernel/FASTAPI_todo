from typing import Dict, List, Union
from controllers.todos_cnt import TodosCnt
from data.schemas.todo import Todo, TodoCreate, TodoDelete, TodoUpdate
from fastapi import APIRouter
router = APIRouter()

todos_cnt = TodosCnt("todos controller")

@router.get('/todos/',tags=["todos"], summary="get all todos")
def get_todos():
    return todos_cnt.get_all()

@router.get('/todo/{id}',tags=["todos"], summary="get a todo", response_model=Todo)
def get_todo(id:str):
    return todos_cnt.get(id)

@router.post('/todos/',tags=["todos"], summary="add a todo")
def add_todos(todo: TodoCreate):
    return todos_cnt.add(todo)

@router.put('/todo/{id}',tags=["todos"], summary="update a todo", response_model=Todo)
def update_todos(id:str, todo: TodoUpdate):
    return todos_cnt.update(id,todo)

@router.delete('/todo/{id}',tags=["todos"], summary="delete a todo")
def delete_todos(id:str):
    return todos_cnt.delete(id)