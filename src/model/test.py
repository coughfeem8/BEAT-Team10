from os import walk
import xmltodict
from model import dbconnection

projectDb = dbconnection.getCollection("plugin")

'''
f = []
for (dirpath, dirnames, filenames) in walk('../plugins'):
    for name in filenames:
        if name.endswith('.xml'):
            f.append(name)
    break
plugins = []
for pl in f:
    with open('../plugins/%s' % pl) as fd:
        doc = xmltodict.parse(fd.read())
        i = doc["plugin"]["name"]
        #print(i)
        projInfo = projectDb[i]
        info = {"name":i,"desc":doc["plugin"]["description"],"poi":doc["plugin"]["point_of_interest"],
                "output":doc["plugin"]["output"]}
        insertInfo = projInfo.insert(info, check_keys=False)
'''
#dbconnection.dropDB("plugin")
print(dbconnection.getDB())
#projectDb = dbconnection.getCollection("plugin")
x = dbconnection.listCOllections("plugin")
for i in x:
    #print(i[])
    projInfo = projectDb[i]
    #binInfo = projectDb["binaryInfo"]
    cursor = projInfo.find()
    for db in cursor:
        print(db["name"])