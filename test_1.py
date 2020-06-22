import pymongo
import random
from mongoengine import *


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["setsgame"]
mycol = mydb["cards"]
connect('cards')

class Card(Documets):
    _id = IntegerField(required=True)
    color = StringField(max_length=50)
    shape = StringField(max_length=50)
    fill_type = StringField(max_length=50)
    Number_of_shapes = StringField(max_length=50)
    l