from pydantic import BaseModel
from graphene_mongo import MongoengineObjectType
from graphene_pydantic import PydanticInputObjectType

from models import Car


# class CarModel(BaseModel):
#     id: str
#     year: int
#     model: str
#     color: str


# class CarGrapheneModel(MongoengineObjectType):
#     class Meta:
#         model = Car


# class CarGrapheneInputModel(PydanticInputObjectType):
#     class Meta:
#         model = CarModel
#         exclude_fields = ('id', )
