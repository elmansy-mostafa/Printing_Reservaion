from backend.models import Reservation
from backend.database import reservations_collection
from bson import ObjectId

async def create_reservation(reservation: Reservation):
    reservation_dict = reservation.dict()
    await reservations_collection.insert_one(reservation_dict)
    return reservation_dict

async def get_reservations():
    reservations = await reservations_collection.find().to_list(length=100)
    return reservations
