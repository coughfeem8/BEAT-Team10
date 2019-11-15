import pymongo
import base64
from model.Singleton import Singleton

global mongoClient
mongoClient = pymongo.MongoClient("mongodb://localhost:27017")


def get_db():
    cursor = mongoClient.list_database_names()
    return cursor


def drop_db(name):
    mongoClient.drop_database(name)


def list_collections(db):
    dbs = mongoClient[db]
    cursor = dbs.list_collection_names()
    return cursor

def get_collection(db):
    project_db = mongoClient[db]
    return project_db


def search_by_item(item):
    s = Singleton.get_project()
    project_db = get_collection(s)
    value = None
    if item.toolTip() == "Functions":
        project_info = project_db["functions"]
        cursor = project_info.find_one({"name": item.text()})
        if cursor is not None:
            value = {"_id":cursor["_id"],'name': cursor["name"], 'signature': cursor["signature"], 'varaddress': hex(cursor["offset"]),
                     'from': cursor["from"], 'comment': cursor["comment"]}
    elif item.toolTip() == "Strings":
        project_info = project_db["string"]
        cursor = project_info.find_one({"string": item.text()})
        if cursor is not None:
            value = {"_id":cursor["_id"],'string': cursor["string"], 'varaddress': hex(cursor["vaddr"]), 'from': cursor["from"],
                     'comment': cursor["comment"]}
    return value
