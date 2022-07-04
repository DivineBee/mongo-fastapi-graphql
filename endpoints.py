# from fastapi import APIRouter
# from config.db import db
# from core.schemas import carsEntity, carEntity
# from core.models import Car
# from bson import ObjectId
#
# car = APIRouter()
#
#
# @car.get('/')
# async def find_all_cars():
#     return carsEntity(db.local.car.find())
#
#
# @car.get('/{id}')
# async def find_one_car(id):
#     return carEntity(db.local.car.find_one({"_id": ObjectId(id)}))
#
#
# @car.post('/')
# async def create_car(car: Car):
#     db.local.car.insert_one(dict(car))
#     return carsEntity(db.local.car.find())
#
#
# @car.put('/{id}')
# async def update_car(id, car: Car):
#     db.local.car.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(car)})
#     return carEntity(db.local.car.find_one({"_id": ObjectId(id)}))
#
#
# @car.delete('/{id}')
# async def delete_car(id):
#     return carEntity(db.local.car.find_one_and_delete({"_id": ObjectId(id)}))
