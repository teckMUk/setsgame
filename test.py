import pymongo
import random



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["setsgame"]
mycol = mydb["cards"]

def find_my_card(id):
         myquery = {"_id" : id}
         for card in mycol.find(myquery):
             return card  
        
class Card():
    def __init__(self,_id,color,shape,fill_type,number_of_shapes,bitlist):
        self._id =_id
        self.color = color
        self.shape = shape
        self.fill_type = fill_type
        self.number_of_shapes = number_of_shapes
        self.bitlist = bitlist
    def random_fun():
         print(self.bitlist)    


class Deck(Card):
    def __init__(self,n=12):
       for number in range(1,n+1):
           x = random.randint(1,81)
           self.cards = find_my_card(x)
           print(self.cards)
           super().__init__(self.cards['_id'],self.cards['color'],self.cards['shape'],self.cards['fill_type'],self.cards['Number of shapes'],self.cards['bitlist'])
                 
       
obj = Deck(12)
print(Card.random_fun)  




