from fastapi import FastAPI;
# from app.routes.todo_routes import router as todo_router
from app.routes.user_routes import router as user_router

app = FastAPI()

app.include_router(user_router)

