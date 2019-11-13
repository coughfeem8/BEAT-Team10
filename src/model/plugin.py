from model import dbconnection

def getInstalled():
    list = []
    x = dbconnection.listCOllections("plugin")
    for i in x:
        list.append(i)
    return list

def getTypes(type, current):
    list = []
    pluginDB = dbconnection.getCollection("plugin")
    currentColl = pluginDB[current]
    cursor = currentColl.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if type == ash["type"]:
                list.append(ash["name"])
    return list

def getName(plugin):
    projectDb = dbconnection.getCollection("plugin")
    x = dbconnection.listCOllections("plugin")
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
    pluginDB = dbconnection.getCollection("plugin")
    currentColl = pluginDB[current]
    cursor = currentColl.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if ash["name"] in item:
                return ash["pythonOutput"]

def updatePOI(list, current):
    print(list)
    pluginDB = dbconnection.getCollection("plugin")
    myCol = pluginDB[current]

    query = {"name": current}
    newValues = {"$set": {"poi":list}}
    myCol.update_one(query,newValues)
    for x in myCol.find():
        print(x)