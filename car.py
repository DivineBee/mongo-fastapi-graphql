import graphene
from graphene_mongo import MongoengineObjectType
import services
from models import Car as CarModel


class Car(MongoengineObjectType):
    class Meta:
        model = CarModel


class Query(graphene.ObjectType):
    cars = graphene.List(Car, skip=graphene.Int(default_value=0), limit=graphene.Int(default_value=5))
    car = graphene.Field(Car, id=graphene.ID(required=True))

    def resolve_cars(self, info, skip, limit):
        return services.get_car_list(skip, limit)

    def resolve_car_count(self, info):
        return services.get_car_count()

    def resolve_car(self, info, id):
        return services.get_car_detail(id)


class CreateCar(graphene.Mutation):
    class Arguments:
        year = graphene.Int(required=True)
        model = graphene.String(default_value="")
        color = graphene.String(default_value="")

    car = graphene.Field(Car)

    def mutate(self, info, year, model, color):
        car = services.create_car(
            year=year,
            model=model,
            color=color,
        )

        return CreateCar(car=car)


class DeleteCar(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    result = graphene.Boolean()

    def mutate(self, info, id):
        result = services.delete_car(id)

        return DeleteCar(result=result)


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    delete_car = DeleteCar.Field()
