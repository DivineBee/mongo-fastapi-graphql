from mongoengine import DoesNotExist, ValidationError
from mongoengine.queryset.queryset import QuerySet

import models


def get_car_list(skip: int, limit: int) -> QuerySet:
    return models.Car.objects.skip(skip).limit(limit).all()


def get_car_count() -> int:
    return models.Car.objects.all().count()


def get_car_detail(id: str) -> models.Car:
    return models.Car.objects.get(id=id)


def create_car(**kwargs: dict) -> models.Car:
    return models.Car(**kwargs).save()


def delete_car(id: str) -> bool:
    try:
        models.Car.objects.get(id=id).delete()
        return True
    except DoesNotExist:
        return False
    except ValidationError:
        return False
