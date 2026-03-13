from fastapi import FastAPI
from app.api.users import router

app = FastAPI()

app.include_router(router,prefix="/users")
