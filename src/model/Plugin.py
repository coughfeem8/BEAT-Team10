from model import DBConnection

def get_installed_plugins():
    list = []
    x = DBConnection.list_collections("plugin")
    for i in x:
        list.append(i)
    return list


def plugin_types(type, current):
    list = []
    pluginDB = DBConnection.get_collection("plugin")
    currentColl = pluginDB[current]
    cursor = currentColl.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if type == ash["type"]:
                list.append(ash["name"])
    return list

def getName(plugin):
    projectDb = DBConnection.get_collection("plugin")
    x = DBConnection.list_collections("plugin")
    for i in x:
        if plugin == i:
            projInfo = projectDb[i]
            cursor = projInfo.find()
            return cursor

def getPOI(plugin):
    cursor = getName(plugin)
    for i in cursor:
        return i["poi"]

def getOutput(item, current):
    pluginDB = DBConnection.get_collection("plugin")
    currentColl = pluginDB[current]
    cursor = currentColl.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if ash["name"] in item:
                return ash["pythonOutput"]

def updatePOI(list, current):
    pluginDB = DBConnection.get_collection("plugin")
    myCol = pluginDB[current]

    query = {"name": current}
    newValues = {"$set": {"poi":list}}
    myCol.update_one(query,newValues)
