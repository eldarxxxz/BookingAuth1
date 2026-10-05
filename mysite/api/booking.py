from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mysite.database.db import get_db
from mysite.database.models import Booking
from mysite.database.schema import BookingInput, BookingOutput


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)



@router.get("/", response_model=list[BookingOutput])
def get_bookings(
    db: Session = Depends(get_db)
):
    return db.query(Booking).all()



@router.get("/{booking_id}", response_model=BookingOutput)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking



@router.post("/", response_model=BookingOutput)
def create_booking(
    booking_data: BookingInput,
    db: Session = Depends(get_db)
):
    booking = Booking(
        user_id=booking_data.user_id,
        hotel_name=booking_data.hotel_name,
        check_in=booking_data.check_in,
        check_out=booking_data.check_out,
        guests=booking_data.guests
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking



@router.put("/{booking_id}", response_model=BookingOutput)
def update_booking(
    booking_id: int,
    booking_data: BookingInput,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.user_id = booking_data.user_id
    booking.hotel_name = booking_data.hotel_name
    booking.check_in = booking_data.check_in
    booking.check_out = booking_data.check_out
    booking.guests = booking_data.guests

    db.commit()
    db.refresh(booking)

    return booking



@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    db.delete(booking)
    db.commit()

    return {
        "message": "Booking deleted successfully"
    }



@router.post("/", response_model=BookingOutput)
def create_booking(
    booking_data: BookingInput,
    db: Session = Depends(get_db)
):
    booking = Booking(
        user_id=booking_data.user_id,
        hotel_name=booking_data.hotel_name,
        check_in=booking_data.check_in,
        check_out=booking_data.check_out,
        guests=booking_data.guests
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking