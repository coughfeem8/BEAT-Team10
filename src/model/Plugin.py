from model import DBConnection

def get_installed_plugins():
    plugins = []
    x = DBConnection.list_collections("plugin")
    for i in x:
        plugins.append(i)
    return plugins

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

def get_name(plugin):
    plugin_db = DBConnection.get_collection("plugin")
    x = DBConnection.list_collections("plugin")
    for i in x:
        if plugin == i:
            info = plugin_db[i]
            cursor = info.find()
            return cursor

def get_poi(plugin):
    cursor = get_name(plugin)
    for i in cursor:
        return i["poi"]

def get_output(item, current):
    plugin_db = DBConnection.get_collection("plugin")
    coll = plugin_db[current]
    cursor = coll.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if ash["name"] in item:
                return ash["pythonOutput"]

def update_poi(list,current):
    plugin_db = DBConnection.get_collection("plugin")
    col = plugin_db[current]
    query = {"name": current}
    newValues = {"$set": {"poi":list}}
    col.update_one(query,newValues)
