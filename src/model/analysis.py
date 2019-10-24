import r2pipe
from model.singleton import Singleton
from model import plugin, dbconnection
import base64


def staticStrings(cplugin):
    rlocal = r2pipe.open(Singleton.getPath())
    rlocal.cmd("aaa")
    items = []
    s = Singleton.getProject()
    projectDb = dbconnection.getCollection(s)
    # Strings
    strings = rlocal.cmdj("izj")
    strplg = plugin.pluginTypes("String", cplugin)

    if projectDb["string"]:
        projectDb.drop_collection("string")

    strDB = projectDb["string"]
    for string in strings:
        text = base64.b64decode(string["string"])
        for i in strplg:
            if i.upper() in text.decode().upper():
                x = rlocal.cmdj("axtj %s" % string["vaddr"])
                ocurrence = []
                for str in x:
                    ocurrence.append(hex(str["from"]))
                items.append(text.decode())
                string["ocurrence"] = ocurrence
                string["comment"] = ""
                strDB.insert_one(string)
                break
    rlocal.quit()
    return items

def staticFunctions(cplugin):
    rlocal = r2pipe.open(Singleton.getPath())
    rlocal.cmd("aaa")
    items = []
    s = Singleton.getProject()
    projectDb = dbconnection.getCollection(s)
    if projectDb["functions"]:
        projectDb.drop_collection("functions")
    funcDB = projectDb["functions"]
    funcAll = rlocal.cmdj("aflj")
    funcplg = plugin.pluginTypes("Function", cplugin)

    for fc in funcAll:

        if fc["name"] in funcplg:
            function = rlocal.cmdj("axtj %s" % fc["name"])
            ocurrence = []
            for f in function:
                ocurrence.append(hex(f["from"]))
            items.append(fc["name"])
            fc["ocurrence"] = ocurrence
            fc["comment"] = ""
            funcDB.insert_one(fc)

    rlocal.quit()
    return items
