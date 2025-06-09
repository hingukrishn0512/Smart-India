from fastapi import FastAPI
from routes.route import app_router

app = FastAPI()

app.include_router(app_router)
