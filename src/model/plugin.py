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