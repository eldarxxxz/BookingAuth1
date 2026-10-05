from datetime import date
from pydantic import BaseModel, EmailStr, ConfigDict
from mysite.database.models import StatusChoices


class UserProfileInput(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr | None = None
    password: str
    phone_number: str | None = None
    age: int
    status: StatusChoices = StatusChoices.simple_user


class UserProfileOutput(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr | None = None
    phone_number: str | None = None
    age: int
    status: StatusChoices
    registered_date: date

    model_config = ConfigDict(from_attributes=True)

    class BookingInput(BaseModel):
        user_id: int
        hotel_name: str
        check_in: date
        check_out: date
        guests: int

    class BookingOutput(BaseModel):
        id: int
        user_id: int
        hotel_name: str
        check_in: date
        check_out: date
        guests: int

        model_config = ConfigDict(from_attributes=True)

class BookingInput(BaseModel):
    user_id: int
    hotel_name: str
    check_in: date
    check_out: date
    guests: int


class BookingOutput(BaseModel):
    id: int
    user_id: int
    hotel_name: str
    check_in: date
    check_out: date
    guests: int

    model_config = ConfigDict(from_attributes=True)