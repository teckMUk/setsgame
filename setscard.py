import pymongo
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["setsgame"]
mycol = mydb["cards"]

dictin = os.listdir('/mnt/c/Users/mukeet/Documents/setsgame')
mylist = [] 
variable = -1
for filename in dictin:
     variable +=1
     total_number_of_dashes =0
     shape = ""
     color = ""
     file_type = ""
     fill_type = ""
     number = ""
     file_path = r"C:\Users\mukeet\Documents\setsgame\ " 
     file_path += filename
     for character in filename:
         if character == '_':
             total_number_of_dashes += 1
         elif character == '.':
             total_number_of_dashes =4    
         elif total_number_of_dashes == 0:
            shape += character
         elif total_number_of_dashes ==1:
             color += character
         elif total_number_of_dashes ==2:
             fill_type += character
         elif total_number_of_dashes ==3:
             number +=character    
         else :
              file_type += character
     mycards_details = {"_id" : variable,
                        "color" : color,
                        "shape" : shape,
                        "fill_type" : fill_type,
                        "image_file_path" : file_path,

     }
     if file_type == "svg":
         mylist.append(mycards_details)

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
