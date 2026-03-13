Q1) 
from fastapi import FastAPI,APIRouter

router = APIRouter()
@router.get("/")
def home():
    retun {"message": "ok"}


Q2)

from fastapi import Depends
from app.core.database import get_db

@router.get("/users")
def get_users(db: Session= Depends(get_db()))


q3)

def get_db():
    db = SessionLocal()
        try:
            yeild db
        finally:
            db.close()

q4)

from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str,
    email:str,
    password:str

q5)
from app.core.database import get_db
from fastapi import HttpException
def get_users(db : Session = Depends(get_db())):
    user = some...query...
    if not user:
        raise HttpException(status_code=404,message : "User not found")



router  =APIRouter()

@router.get("/")
def home():
    return {"message":"ok"}


def get_db():
    db = SessionLocal()
    try:
        yeild db
    finally:
        db.close()

raise HttpException(status_code=404, detail ="data not found")