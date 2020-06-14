import pymongo
import random
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["setsgame"]
mycol = mydb["cards"]

def find_my_card(id_number):
    myquery = {"_id" : id_number}
    for card in mycol.find(myquery):
        print(card)
        


def draw_12_card():
    for number in range(1,13):
        x = random.randint(1,81)
        find_my_card(x)
        


draw_12_card()