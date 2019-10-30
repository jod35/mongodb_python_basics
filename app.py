from pymongo import MongoClient
import pprint

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

# result1=dogs.insert_many(dogs_array)
# print(result1)

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
# dog =dogs.find_one()
# print(dog)
# {'_id': ObjectId('5db9cf8bd9fd9777d9c879e2'), 'name': 'Doggy', 'age': 3, 'specie': 'German Shepherd', 'owner': 'jona'}

#retrieving many documents

many_dogs=dogs.find()
# print(many_dogs)
#returns a cursor object
# <pymongo.cursor.Cursor object at 0x033E6E50>

#to show all documents,we use pprint to print them out like so
# for dog in many_dogs:
#     pprint.pprint(dog)

# {'_id': ObjectId('5db9cf8bd9fd9777d9c879e2'),
#  'age': 3,
#  'name': 'Doggy',
#  'owner': 'jona',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9cf90940d32730d70926c'),
#  'age': 3,
#  'name': 'Doggy',
#  'owner': 'jona',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d1149805b9ac8f609304'),
#  'age': 3,
#  'name': 'Doggy',
#  'owner': 'jona',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d33f4a5e8c8740974898'),
#  'age': 2,
#  'name': 'Bob',
#  'owner': 'Jannet',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d33f4a5e8c8740974899'),
#  'age': 7,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d33f4a5e8c874097489a'),
#  'age': 6,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'Geared'}
# {'_id': ObjectId('5db9d33f4a5e8c874097489b'),
#  'age': 5,
#  'name': 'Bobby',
#  'owner': 'James',
#  'specie': 'St Benard'}
# {'_id': ObjectId('5db9d33f4a5e8c874097489c'),
#  'age': 5,
#  'name': 'Babbie',
#  'owner': 'Jeremiah',
#  'specie': 'Rotweiler'}
# {'_id': ObjectId('5db9d4ae0deea34f567c5aba'),
#  'age': 2,
#  'name': 'Bob',
#  'owner': 'Jannet',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d4ae0deea34f567c5abb'),
#  'age': 7,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d4ae0deea34f567c5abc'),
#  'age': 6,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'Geared'}
# {'_id': ObjectId('5db9d4ae0deea34f567c5abd'),
#  'age': 5,
#  'name': 'Bobby',
#  'owner': 'James',
#  'specie': 'St Benard'}
# {'_id': ObjectId('5db9d4ae0deea34f567c5abe'),
#  'age': 5,
#  'name': 'Babbie',
#  'owner': 'Jeremiah',
#  'specie': 'Rotweiler'}
# {'_id': ObjectId('5db9d723ddda9b2e95c84f15'),
#  'age': 2,
#  'name': 'Bob',
#  'owner': 'Jannet',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d723ddda9b2e95c84f16'),
#  'age': 7,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d723ddda9b2e95c84f17'),
#  'age': 6,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'Geared'}
# {'_id': ObjectId('5db9d723ddda9b2e95c84f18'),
#  'age': 5,
#  'name': 'Bobby',
#  'owner': 'James',
#  'specie': 'St Benard'}
# {'_id': ObjectId('5db9d723ddda9b2e95c84f19'),
#  'age': 5,
#  'name': 'Babbie',
#  'owner': 'Jeremiah',
#  'specie': 'Rotweiler'}
# {'_id': ObjectId('5db9d79aa47bd31c22d9c8c2'),
#  'age': 2,
#  'name': 'Bob',
#  'owner': 'Jannet',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d79aa47bd31c22d9c8c3'),
#  'age': 7,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'German Shepherd'}
# {'_id': ObjectId('5db9d79aa47bd31c22d9c8c4'),
#  'age': 6,
#  'name': 'Bob',
#  'owner': 'Walter',
#  'specie': 'Geared'}
# {'_id': ObjectId('5db9d79aa47bd31c22d9c8c5'),
#  'age': 5,
#  'name': 'Bobby',
#  'owner': 'James',
#  'specie': 'St Benard'}
# {'_id': ObjectId('5db9d79aa47bd31c22d9c8c6'),
#  'age': 5,
#  'name': 'Babbie',
#  'owner': 'Jeremiah',
#  'specie': 'Rotweiler'}

