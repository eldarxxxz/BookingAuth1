from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mysite.database.db import get_db
from mysite.database.models import UserProfile
from mysite.database.schema import UserProfileInput, UserProfileOutput
from mysite.api.auth import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[UserProfileOutput])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserProfile).all()
    return users



@router.get("/{user_id}", response_model=UserProfileOutput)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserProfile = Depends(get_current_user)
):
    user = db.query(UserProfile).filter(
        UserProfile.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put("/{user_id}", response_model=UserProfileOutput)
def update_user(
        user_id: int,
        user_data: UserProfileInput,
        db: Session = Depends(get_db)
):
    user = db.query(UserProfile).filter(UserProfile.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.first_name = user_data.first_name
    user.last_name = user_data.last_name
    user.username = user_data.username
    user.email = user_data.email
    user.password = user_data.password
    user.phone_number = user_data.phone_number
    user.age = user_data.age
    user.status = user_data.status

    db.commit()
    db.refresh(user)

    return user



@router.delete("/{user_id}")
def delete_user(
        user_id: int,
        db: Session = Depends(get_db)
):
    user = db.query(UserProfile).filter(UserProfile.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }