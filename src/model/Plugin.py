import xmltodict
from os import walk
from model.Singleton import Singleton


def plugin_connection(current):
    for pl in Singleton.get_plugins():
        with open('plugins/%s' % pl) as fd:
            doc = xmltodict.parse(fd.read())
            if doc["plugin"]["name"] == current:
                break
    return doc


def get_plugin_file(current):
    for pl in Singleton.get_plugins():
        with open('plugins/%s' % pl) as fd:
            doc = xmltodict.parse(fd.read())
            if doc["plugin"]["name"] == current:
                break
    return pl


def get_installed_plugins():
    plugins = []
    for pl in Singleton.get_plugins():
        with open('plugins/%s' % pl) as fd:
            doc = xmltodict.parse(fd.read())
            i = doc["plugin"]["name"]
            plugins.append(i)
    return plugins


def plugin_types(type, current):
    plugin = plugin_connection(current)
    items = []

    for i in plugin["plugin"]["point_of_interest"]["item"]:
        if type == i["type"]:
            items.append(i["name"])
    return items


def set_plugins():
    f = []
    for (dirpath, dirnames, filenames) in walk('./plugins'):
        for name in filenames:
            if name.endswith('.xml'):
                f.append(name)
        break
    Singleton.set_plugins(f)