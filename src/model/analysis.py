import r2pipe
from model.singleton import Singleton
from model import plugin, dbconnection
import base64
from PyQt5 import QtCore

def staticAll(path):
    rlocal = r2pipe.open(path)
    rlocal.cmd("aaa")
    return rlocal

def staticStrings(rlocal, cplugin):
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
    return items

def staticFunctions(rlocal, cplugin):
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

    return items




class AThread(QtCore.QThread):
    textSignal = QtCore.pyqtSignal(str)

    def __init__(self, rlocal):
        super(AThread, self).__init__()
        self.rlocal = rlocal


    def run(self):
        while True:

            x = self.rlocal.cmd("dc")

            if "Cannot continue, run ood?" in x:
                break
            self.textSignal.emit(x)
            y = self.rlocal.cmd("dso")
            self.textSignal.emit(y)
            messageAddr = self.rlocal.cmd("dr rsi")  # Memory location to what recv received is in register rsi.

            lookInBuff = "pxj @" + messageAddr  # create command to get contents of memory where recv received a message.

            messageArr = self.rlocal.cmdj(lookInBuff)  # get contents of memory where recv received a message.

            byteStr = ""  # variable that will hold hex values of message

            # Loop over byte array and remove each hex value (ie each letter sent in message)
            for i in range(len(messageArr)):

                # If found 0 byte...then is end of message in memory.
                if messageArr[i] == 0:
                    break
                # building byte string.
                byteStr = byteStr + str(hex(messageArr[i]))[2:] + " "

            if "ff ff ff ff" not in byteStr:
                self.textSignal.emit(byteStr)