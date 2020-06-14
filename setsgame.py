import pymongo
import random


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["setsgame"]
mycol = mydb["cards"]

def find_my_card(id_number):
    myquery = {"_id" : id_number}
    for card in mycol.find(myquery):
        return card



def draw_12_card():
    for number in range(1,13):
        x = random.randint(1,81)
        print(find_my_card(x))
        
def set_finder(id_1,id_2,id_3):
    card_1 = find_my_card(int(id_1))
    card_2 = find_my_card(int(id_2))
    card_3 = find_my_card(int(id_3))
    set_or_not = True
    if card_1['color'] == card_2['color'] and card_1['color'] != card_3['color']:
        set_or_not = False
    elif card_1['color'] != card_2['color'] and card_1['color'] == card_3['color']:
        set_or_not = False
    if card_1['shape'] == card_2['shape']  and card_1['shape'] != card_3['shape']:
        set_or_not = False
    elif card_1['shape'] != card_2['shape']  and card_1['shape'] == card_3['shape']:
        set_or_not = False
    if card_1['fill_type'] == card_2['fill_type']  and card_1['fill_type'] != card_3['fill_type']:
        set_or_not = False
    elif card_1['fill_type'] != card_2['fill_type']  and card_1['fill_type'] == card_3['fill_type']:
        set_or_not = False
    if card_1['Number of shapes'] == card_2['Number of shapes']  and card_1['Number of shapes'] != card_3['Number of shapes']:
        set_or_not = False
    elif card_1['Number of shapes'] != card_2['Number of shapes']  and card_1['Number of shapes'] == card_3['Number of shapes']:
        set_or_not = False    
    if set_or_not == True:
        print("it's a set")
    else:
        print("not a set")        


draw_12_card()
val = input("Enter _id of 3 cards seprated by space :" )
user_id_number = val.split(" ")
id_1 = user_id_number[0]
id_2 = user_id_number[1]
id_3 = user_id_number[2]
set_finder(id_1,id_2,id_3)