from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status

from core import tasks, users
from schemas import Task, User

app = FastAPI()


def get_current_user(username: str, password: str):
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                return User.model_validate(user)


@app.get("/tasks/")
async def get_tasks_for_user():
    """
    Получает все задачи пользователя
    """


if __name__ == "__main__":
    uvicorn.run(app)
