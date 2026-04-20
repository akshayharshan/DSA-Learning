from fastapi import FastAPI,Depends
from app.core.database import get_db,Base
from api.routes import router


app = FastAPI()
app.include_router(router)
