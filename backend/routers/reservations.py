from fastapi import APIRouter, HTTPException
from backend.models import Reservation, AvailableSlot
from backend.crud import create_reservation, get_reservations
from backend.utils import export_to_excel
from datetime import datetime, timedelta
from typing import List

router = APIRouter()

# Predefined available slots
def generate_available_slots():
    available_slots = {
        "it": ["Saturday 9:00 AM", "Saturday 11:00 AM", "Tuesday 9:00 AM", "Tuesday 11:00 AM"],
        "industrial": ["Sunday 9:00 AM", "Wednesday 9:00 AM"],
        "health": ["Monday 9:00 AM", "Thursday 9:00 AM"]
    }
    return available_slots

@router.get("/slots/{department}", response_model=AvailableSlot)
async def get_slots(department: str):
    available_slots = generate_available_slots()
    if department not in available_slots:
        raise HTTPException(status_code=400, detail="Invalid department")
    
    slots = available_slots[department]
    return AvailableSlot(department=department, slots=slots)

@router.post("/reserve")
async def reserve_slot(reservation: Reservation):
    # Save reservation in DB
    await create_reservation(reservation)
    return {"message": "Reservation successful"}

@router.get("/reservations")
async def view_reservations():
    reservations = await get_reservations()
    return {"reservations": reservations}

@router.get("/export")
async def export_reservations():
    reservations = await get_reservations()
    return export_to_excel(reservations)
