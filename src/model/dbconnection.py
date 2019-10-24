import pymongo


global mongoClient
mongoClient = pymongo.MongoClient("mongodb://localhost:27017")

def getDB():
    cursor = mongoClient.list_database_names()
    return cursor

def dropDB(name):
    mongoClient.drop_database(name)

def getCollection(db):
    projectDb = mongoClient[db]
    return projectDb