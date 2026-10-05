from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from mysite.database.db import get_db
from mysite.database.models import UserProfile
from mysite.database.schema import UserProfileOutput


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users", response_model=list[UserProfileOutput])
def admin_users(db: Session = Depends(get_db)):
    users = db.query(UserProfile).all()
    return users