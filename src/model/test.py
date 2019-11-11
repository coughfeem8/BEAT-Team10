from os import walk
import xmltodict
from model import plugin, dbconnection

dbconnection.dropDB("plugin")


#x = plugin.getName("Network")
#for i in x:
#    print(i)