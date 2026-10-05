from datetime import date
from enum import Enum
from sqlalchemy import String, Integer, Date, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column
from mysite.database.db import Base


class StatusChoices(str, Enum):
    simple_user = "simple_user"
    hotel_owner = "hotel_owner"


class UserProfile(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(40))

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    email: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    password: Mapped[str] = mapped_column(String(255))

    phone_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    age: Mapped[int] = mapped_column(Integer)

    status: Mapped[StatusChoices] = mapped_column(
        SqlEnum(StatusChoices),
        default=StatusChoices.simple_user
    )

    registered_date: Mapped[date] = mapped_column(
        Date,
        default=date.today
    )

from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    hotel_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    check_in: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    check_out: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    guests: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

