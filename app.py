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

# dog ={
#     'name':"Doggy",
#     'age':3,
#     'specie':'German Shepherd',
#     'owner':'jona'
# }

# #insert the document in the database
# result=dogs.insert_one(dog)

# if result.acknowledged:
#     print('Course Added successfully and its ID is ',result.inserted_id)
#     # Course Added successfully and its ID is  5db9d1149805b9ac8f609304


# inserting many documents
dogs_array=[
    {
        'name':'Bob',
        'specie':'German Shepherd',
        'age':2,
        'owner':'Jannet'
    },
     {
        'name':'Bob',
        'specie':'German Shepherd',
        'age':7,
        'owner':'Walter'
    }, {
        'name':'Bob',
        'specie':'Geared',
        'age':6,
        'owner':'Walter'
    }, {
        'name':'Bobby',
        'specie':'St Benard',
        'age':5,
        'owner':'James'
    },
     {
        'name':'Babbie',
        'specie':'Rotweiler',
        'age':5,
        'owner':'Jeremiah'
    }
]

result1=dogs.insert_many(dogs_array)
print(result1)

# <pymongo.results.InsertManyResult object at 0x03046738>

# printing inserted ids
# for object_id in result1.inserted_ids:
#     print(object_id)

# <pymongo.results.InsertManyResult object at 0x02E4F2D8>
# 5db9d4ae0deea34f567c5aba
# 5db9d4ae0deea34f567c5abb
# 5db9d4ae0deea34f567c5abc
# 5db9d4ae0deea34f567c5abd
# 5db9d4ae0deea34f567c5abe

#retriving one document
dog =dogs.find_one()
print(dog)
# {'_id': ObjectId('5db9cf8bd9fd9777d9c879e2'), 'name': 'Doggy', 'age': 3, 'specie': 'German Shepherd', 'owner': 'jona'}