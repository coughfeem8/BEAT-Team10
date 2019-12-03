import base64

from model import r2Connection, DBConnection, Plugin
from model.Singleton import Singleton


def static_all(path):
    """
    Opens a connection to Radare2 and Analysis all
    :param path: String path of the binary file
    :return: R2Connection
    """
    rlocal = r2Connection.Open(path)
    rlocal.cmd("aaa")
    return rlocal


def static_strings(rlocal, cplugin):
    """
    Analysis all the strings in the binary and filters with nthe selected plugin and adds them to the database
    :param rlocal: R2Connection of the binary file
    :param cplugin: string current selected plugin
    :return: List of dict with filtered strings
    """
    items = []
    s = Singleton.get_project()
    project_db = DBConnection.get_collection(s)
    # Strings
    strings = rlocal.cmdj("izj")
    str_plg = Plugin.plugin_types("String", cplugin)

    #if project_db["string"]:
    #    project_db.drop_collection("string")

    str_db = project_db["string"]
    for string in strings:
        text = string["string"]
        text_decoded = base64.b64decode(text)
        for i in str_plg:
            if i.upper() in text_decoded.decode().upper():
                x = rlocal.cmdj("axtj %s" % string["vaddr"])
                tmp = text_decoded.decode()
                for str in x:
                    string["string"] = tmp + " " + hex(str["from"])
                    items.append(string["string"])
                    string["from"] = hex(str["from"])
                    string["comment"] = ""
                    if "_id" in string:
                        del string["_id"]
                    if str_db.find({"string":string["string"]}).count() == 0:
                        str_db.insert_one(string)
                break
    return items


def static_functions(rlocal, cplugin):
    """
    Analysis all the functions in the binary and filters with the selected plugin and adds them to the database
    :param rlocal: R2Connection of the binary file
    :param cplugin: string current selected plugin
    :return: List of dict with filtered functions
    """
    items = []
    s = Singleton.get_project()
    project_db = DBConnection.get_collection(s)

    #if project_db["functions"]:
    #    project_db.drop_collection("functions")

    func_db = project_db["functions"]
    func_all = rlocal.cmdj("aflj")
    func_plg = Plugin.plugin_types("Function", cplugin)

    for fc in func_all:

        if fc["name"] in func_plg:
            function = rlocal.cmdj("axtj %s" % fc["name"])
            tmp = fc["name"]
            for f in function:
                fc["name"] = tmp + " " + hex(f["from"])
                items.append(fc["name"])
                fc["comment"] = ""
                fc["runs"] = []
                fc["from"] = hex(f["from"])
                if "_id" in fc:
                    del fc["_id"]
                if func_db.find({"name":fc["name"]}).count() == 0:
                    func_db.insert_one(fc)
    return items
