import pymongo
client = pymongo.MongoClient("mongodb+srv://thanosuniverse143:realme_8@cluster0.frlm8ah.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}

d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}
d = {"name" : "aditya" , "surname" : "dubey" , "email" : "aditya@ineuron"}

db1 = client['Mongotest']
coll = db1['test']
coll.insert_one(d)