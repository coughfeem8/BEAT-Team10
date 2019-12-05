from model.project import DBConnection


def get_installed_plugins():
    """
    Get plugins installed in the database collection 'plugin'
    :return: list of installed plugins
    """
    plugin_list = []
    x = DBConnection.list_collections("plugin")
    for i in x:
        plugin_list.append(i)
    return plugin_list


def plugin_types(plugin_types, current):
    """
    Filters the pois installed in the current plugin with the string passed
    :param plugin_types: string with the type of poi
    :param current: Current selected plugin
    :return: list of pois that matches the type
    """
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
    """
    Gets the information and pois from the selected plugin
    :param plugin: current selected plugin
    :return: Mongo cursor with the info from the plugin
    """
    project_db = DBConnection.get_collection("plugin")
    x = DBConnection.list_collections("plugin")
    for i in x:
        if plugin == i:
            project_info = project_db[i]
            cursor = project_info.find()
            return cursor


def get_poi(plugin):
    """
    Get the pois of the selected plugin
    :param plugin: string selected plugin
    :return: list of dicts with pois
    """
    cursor = get_name(plugin)
    if cursor:
        for i in cursor:
            return i["poi"]


def get_output(item, current):
    """
    Get the output of the poi in the current plugin
    :param item: string name of poi
    :param current: string selected plugin
    :return: string output of poi
    """
    plugin_db = DBConnection.get_collection("plugin")
    current_coll = plugin_db[current]
    cursor = current_coll.find()
    for y in cursor:
        poi = y["poi"]["item"]
        for ash in poi:
            if ash["name"] in item:
                return ash["pythonOutput"]


def get_file(current):
    """
    Get the output file of the selected plugin
    :param current: string current selected plugin
    :return: string path of output file of plugin
    """
    plugin_db = DBConnection.get_collection("plugin")
    coll = plugin_db[current]
    cursor = coll.find()
    for y in cursor:
        out = y["output"]
        return out


def update_poi(poi_list, current):
    """
    Updates pois list in the selected plugin
    :param poi_list: list new pois to add
    :param current: string current selected plugin
    :return: None
    """
    plugin_db = DBConnection.get_collection("plugin")
    my_col = plugin_db[current]

    query = {"name": current}
    new_values = {"$set": {"poi": poi_list}}
    my_col.update_one(query, new_values)


def delete_poi(current, pois):
    """
    Delete the selected poi in the selected plugin
    :param current: string slected plugin
    :param pois: string name of poi
    :return: None
    """
    poi = get_poi(current)
    for i in range(len(poi["item"])):
        if poi["item"][i]['name'] == pois:
            del poi["item"][i]
            break
    update_poi(poi, current)
