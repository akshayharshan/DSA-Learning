from fastapi import APIRouter,Depends
from app.core.database import get_db
from app.models.user import UserCreate,UserResponse
from fastapi import HTTPException

router = APIRouter()

@router.get("/", response_model=UserResponse )
def get_users(db = Depends(get_db)):
    return ["user1", "user2"]
    if not user:
        raise HTTPException(status_code=404, details="User not found")

@router.post("/")
def create_user(data: UserCreate):
    return