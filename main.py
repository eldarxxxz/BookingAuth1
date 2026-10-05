from fastapi import FastAPI
from mysite.api.user import router as user_router
from mysite.api.auth import router as auth_router
from mysite.api.booking import router as booking_router
from mysite.admin.views import router as admin_router
from mysite.database.db import engine, Base


app = FastAPI(
    title="BookingServiceAuth1"
)


Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(auth_router)
app.include_router(booking_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return {
        "message": "BookingServiceAuth1 API is working"
    }