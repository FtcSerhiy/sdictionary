from fastapi import FastAPI
from routers import lesson

app = FastAPI()

app.include_router(lesson.router)