import r2pipe
from model.Singleton import Singleton
from model import Plugin, DBConnection
import base64


def static_all(path):
    rlocal = r2pipe.open(path)
    rlocal.cmd("aaa")
    return rlocal


def static_strings(rlocal, cplugin):
    items = []
    s = Singleton.get_project()
    project_db = DBConnection.get_collection(s)
    # Strings
    strings = rlocal.cmdj("izj")
    str_plg = Plugin.plugin_types("String", cplugin)

    if project_db["string"]:
        project_db.drop_collection("string")

    str_db = project_db["string"]
    for string in strings:
        text = base64.b64decode(string["string"])
        for i in str_plg:
            if i.upper() in text.decode().upper():
                x = rlocal.cmdj("axtj %s" % string["vaddr"])
                ocurrence = []
                for str in x:
                    ocurrence.append(hex(str["from"]))
                items.append(text.decode())
                string["ocurrence"] = ocurrence
                string["comment"] = ""
                str_db.insert_one(string)
                break
    return items


def static_functions(rlocal, cplugin):
    items = []
    s = Singleton.get_project()
    project_db = DBConnection.get_collection(s)
    if project_db["functions"]:
        project_db.drop_collection("functions")
    func_db = project_db["functions"]
    func_all = rlocal.cmdj("aflj")
    func_plg = Plugin.plugin_types("Function", cplugin)

    for fc in func_all:

        if fc["name"] in func_plg:
            function = rlocal.cmdj("axtj %s" % fc["name"])
            ocurrence = []
            for f in function:
                ocurrence.append(hex(f["from"]))
            items.append(fc["name"])
            fc["ocurrence"] = ocurrence
            fc["comment"] = ""
            func_db.insert_one(fc)

    return items


def add_breakpoints_functions(list, rlocal):
    for i in range(len(list)):
        r2breakpoint = 'db' + hex(list[i]["from"])
        rlocal.cmd(r2breakpoint)
