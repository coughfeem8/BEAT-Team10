import pymongo
import base64
from model.project.Singleton import Singleton

global mongo_client
mongo_client = pymongo.MongoClient("mongodb://localhost:27017")


def get_db():
    """
    Gets all the databases in the local mongo server
    :return: Mongo cursor with dbs names
    """
    cursor = mongo_client.list_database_names()
    return cursor


def drop_db(name):
    """
    Deletes the database from the server
    :param name: string Name of database
    :return: None
    """
    mongo_client.drop_database(name)


def list_collections(db):
    """
    List the collections in a Database
    :param db: string name of database
    :return: Mongo cursor
    """
    dbs = mongo_client[db]
    cursor = dbs.list_collection_names()
    return cursor


def get_collection(db):
    """
    Gets the collections of a database
    :param db: String name of database
    :return: MOngo collection
    """
    project_db = mongo_client[db]
    return project_db


def search_by_name(name, type):
    """
    Gets all the information of poi from the database
    :param name: String name of poi
    :param type: String type of the poi
    :return: Dict with all poi info
    """
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
    """
    Gets all the information of a poi from a listwidget item
    :param item: ListwidgetItem selected poi
    :return: dict with pois info
    """
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

def search_comment_by_item(item):
    """
    Gets boolean if there is a comment in the poi from a ListWidgetItem from the database
    :param item: ListWidgetItem selected poi
    :return: Boolean
    """
    value = search_by_item(item)
    if value:
        if value["comment"] == "":
            return False
        return True
    return None