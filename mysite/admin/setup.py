from fastapi import FastAPI
from sqlalchemy.orm import Session
from mysite.database.db import SessionLocal
from mysite.database.models import UserProfile


def get_admin_users():
    db: Session = SessionLocal()

    try:
        return db.query(UserProfile).all()
    finally:
        db.close()