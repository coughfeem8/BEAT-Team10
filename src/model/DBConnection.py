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
                     'ocurrence': cursor["ocurrence"], 'comment': cursor["comment"]}
    elif item.toolTip() == "Strings":
        project_info = project_db["string"]
        text = base64.b64encode(item.text().encode())
        cursor = project_info.find_one({"string": text.decode()})
        if cursor is not None:
            value = {"_id":cursor["_id"],'string': text, 'varaddress': hex(cursor["vaddr"]), 'ocurrence': cursor["ocurrence"],
                     'comment': cursor["comment"]}
    return value
