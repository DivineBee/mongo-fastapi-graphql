# def carEntity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "model": str(item["model"]),
#         "year": str(item["year"]),
#         "color": str(item["color"]),
#     }
#
#
# def carsEntity(entity) -> list:
#     return [carEntity(item) for item in entity]
#
#
# # instead of creating a separate entity for each model like carEntity below code for any model
# # replace carEntity with serializeDict in endpoints
# def serializeDict(a) -> dict:
#     return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}
#
# # replace carsEntity with serializeList in endpoints
# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]
#
#
