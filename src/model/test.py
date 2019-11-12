from os import walk
import xmltodict
from model import plugin, dbconnection, r2connection

dbconnection.dropDB("plugin")
