from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')

db=client['shop']


products=db.products
print(products)

name=input("enter")