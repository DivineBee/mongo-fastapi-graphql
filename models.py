from mongoengine import Document
from mongoengine.fields import StringField, IntField


class Car(Document):
    meta = {'collection': 'cars'}
    year = IntField(required=False)
    model = StringField(required=False)
    color = StringField(required=False)

