from model import DBConnection


def get_installed_plugins():
    plugin_list = []
    x = DBConnection.list_collections("plugin")
    for i in x:
        plugin_list.append(i)
    return plugin_list


def plugin_types(plugin_types, current):
    plugin_list = []
    plugin_db = DBConnection.get_collection("plugin")
    current_coll = plugin_db[current]
    cursor = current_coll.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if plugin_types == ash["type"]:
                plugin_list.append(ash["name"])
    return plugin_list


def get_name(plugin):
    project_db = DBConnection.get_collection("plugin")
    x = DBConnection.list_collections("plugin")
    for i in x:
        if plugin == i:
            project_info = project_db[i]
            cursor = project_info.find()
            return cursor


def get_poi(plugin):
    cursor = get_name(plugin)
    if cursor:
        for i in cursor:
            return i["poi"]


def get_output(item, current):
    plugin_db = DBConnection.get_collection("plugin")
    current_coll = plugin_db[current]
    cursor = current_coll.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if ash["name"] in item:
                return ash["pythonOutput"]


def get_file(current):
    plugin_db = DBConnection.get_collection("plugin")
    coll = plugin_db[current]
    cursor = coll.find()
    for y in cursor:
        out = y["output"]
        return out


def update_poi(poi_list, current):
    plugin_db = DBConnection.get_collection("plugin")
    my_col = plugin_db[current]

    query = {"name": current}
    new_values = {"$set": {"poi": poi_list}}
    my_col.update_one(query, new_values)


def delete_poi(current, pois):
    poi = get_poi(current)
    for i in range(len(poi["item"])):
        if poi["item"][i]['name'] == pois:
            del poi["item"][i]
            break
    update_poi(poi, current)
