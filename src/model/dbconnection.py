import pymongo
import base64
from model.singleton import Singleton

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

def searchByItem(item):
    s = Singleton.getProject()
    projectDb = getCollection(s)
    value = None
    if item.toolTip() == "Functions":
        projInfo = projectDb["functions"]
        cursor = projInfo.find_one({"name": item.text()})
        if cursor is not None:
            value = {"_id":cursor["_id"],'name': cursor["name"], 'signature': cursor["signature"], 'varaddress': hex(cursor["offset"]),
                     'ocurrence': cursor["ocurrence"], 'comment': cursor["comment"]}
    elif item.toolTip() == "Strings":
        projInfo = projectDb["string"]
        text = base64.b64encode(item.text().encode())
        cursor = projInfo.find_one({"string": text.decode()})
        if cursor is not None:
            value = {"_id":cursor["_id"],'string': text, 'varaddress': hex(cursor["vaddr"]), 'ocurrence': cursor["ocurrence"],
                     'comment': cursor["comment"]}
    return value