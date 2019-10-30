from pymongo import MongoClient

#connecting to mongodb on localhost:27017
client =MongoClient('localhost',27017)
#print (client)
# MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

#creating a database
db=client['mydb']
# print(db)
# Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'mydb')

#creating a collection in the database
dogs=db.dogs

# print(dogs)
# Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'mydb'), 'dogs')

#creating a docment

dog ={
    'name':"Doggy",
    'age':3,
    'specie':'German Shepherd',
    'owner':'jona'
}

#insert the document in the database
result=dogs.insert_one(dog)

print(result)