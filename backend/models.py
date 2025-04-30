from typing import List
from pydantic import BaseModel
from datetime import datetime

class Reservation(BaseModel):
    name: str
    subject: str
    department: str
    timeSlot: str

class AvailableSlot(BaseModel):
    department: str
    slots: List[str]
