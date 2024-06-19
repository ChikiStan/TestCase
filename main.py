from fastapi import FastAPI, HTTPException, Depends, status
from core import users, tasks
from schemas import User, Task
import uvicorn
from typing import Annotated



app = FastAPI()

async def get_current_user(username: str, password: str):
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                return User.model_validate(user)
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    

@app.get("/tasks/")
async def get_tasks_for_user(user: Annotated[User,Depends(get_current_user)]):
    """
    Получает все задачи пользователя
    """



if __name__ == "__main__":
    uvicorn.run(app)