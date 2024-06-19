from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str

class Task(BaseModel):
    title: str
    user_id: int