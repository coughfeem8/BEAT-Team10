import pymongo
import base64
from model.Singleton import Singleton

global mongo_client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017")


def get_db():
    cursor = mongo_client.list_database_names()
    return cursor


def drop_db(name):
    mongo_client.drop_database(name)


def list_collections(db):
    dbs = mongo_client[db]
    cursor = dbs.list_collection_names()
    return cursor


def get_collection(db):
    project_db = mongo_client[db]
    return project_db


def search_by_name(name, type):
    s = Singleton.get_project()
    project_db = get_collection(s)
    value = None
    if type == "Functions":
        project_info = project_db["functions"]
        cursor = project_info.find_one({"name": name})
        if cursor is not None:
            value = {"_id": cursor["_id"], 'name': cursor["name"], 'signature': cursor["signature"],
                     'varaddress': hex(cursor["offset"]), 'from': cursor["from"], 'comment': cursor["comment"], 'runs':cursor["runs"]}
    return value


def search_by_item(item):
    if item is not None:
        s = Singleton.get_project()
        project_db = get_collection(s)
        value = None
        if item.toolTip() == "Functions":
            project_info = project_db["functions"]
            cursor = project_info.find_one({"name": item.text()})
            if cursor is not None:
                value = {"_id":cursor["_id"],'name': cursor["name"], 'signature': cursor["signature"], 'varaddress': hex(cursor["offset"]),
                         'from': cursor["from"], 'comment': cursor["comment"],"runs": cursor["runs"]}
        elif item.toolTip() == "Strings":
            project_info = project_db["string"]
            cursor = project_info.find_one({"string": item.text()})
            if cursor is not None:
                value = {"_id":cursor["_id"],'string': cursor["string"], 'varaddress': hex(cursor["vaddr"]), 'from': cursor["from"],
                         'comment': cursor["comment"]}
        return value
    return None
