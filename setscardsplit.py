import os
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["setsgame"]
mycol = mydb["cards"]

dictin = os.listdir("/mnt/c/Users/mukeet/Documents/setsgame")
mylist = []
variable = 0

for filename in dictin:
    filedetails = filename.split("_")
    if len(filedetails) != 1:
        variable += 1
        shape = filedetails[0]
        color = filedetails[1]
        fill_type = filedetails[2]
        mycards_details = {
            "_id": variable,
            "color": color,
            "shape": shape,
            "fill_type": fill_type,
            "file_name": filename,
        }
        mylist.append(mycards_details)
x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)
