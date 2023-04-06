from pydantic import BaseModel, Field
from typing import Optional

class TodoBase(BaseModel):
    title: str
    content: str

    def json(self, *args, **kwargs):
        return self.dict(*args, **kwargs)

class TodoCreate(TodoBase):
    id: Optional[str] = Field(None)
    completed: Optional[bool] = Field(None)

class TodoUpdate(TodoBase):
    id: Optional[str] = Field(None)
    completed:bool

class TodoDelete(TodoBase):
    id:str

class Todo(TodoBase):
    id:str
    completed: Optional[bool] = Field(None)
