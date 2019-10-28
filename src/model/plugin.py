import xmltodict
from os import walk
from model.singleton import Singleton

def pluginConnection(current):
    for pl in Singleton.getPlugins():
        with open('plugins/%s' % pl) as fd:
            doc = xmltodict.parse(fd.read())
            if doc["plugin"]["name"] == current:
                break
    return doc

def getPluginFile(current):
    for pl in Singleton.getPlugins():
        with open('plugins/%s' % pl) as fd:
            doc = xmltodict.parse(fd.read())
            if doc["plugin"]["name"] == current:
                break
    return pl

def getInstalledPlugins():
    plugins = []
    for pl in Singleton.getPlugins():
        with open('plugins/%s' % pl) as fd:
            doc = xmltodict.parse(fd.read())
            i = doc["plugin"]["name"]
            plugins.append(i)
    return plugins

def pluginTypes(type, current):
    plugin = pluginConnection(current)
    items = []

    for i in plugin["plugin"]["point_of_interest"]["item"]:
        if type == i["type"]:
            items.append(i["name"])
    return items

def setPlugins():
    f = []
    for (dirpath, dirnames, filenames) in walk('./plugins'):
        for name in filenames:
            if name.endswith('.xml'):
                f.append(name)
        break
    Singleton.setPlugins(f)