from os import walk
import xmltodict
from model import plugin
with open("../plugins/network.xml") as fd:
    doc = xmltodict.parse(fd.read())
    print(doc)