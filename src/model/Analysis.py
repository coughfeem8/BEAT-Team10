from PyQt5 import QtCore
from model.Singleton import Singleton
from model import Plugin, DBConnection, r2Connection
import base64


def static_all(path):
    rlocal = r2Connection.Open(path)
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
                tmp = text.decode()
                for str in x:
                    string["string"] = tmp + " " + hex(str["from"])
                    items.append(string["string"])
                    string["from"] = hex(str["from"])
                    string["comment"] = ""
                    if "_id" in string:
                        del string["_id"]
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
            tmp = fc["name"]
            for f in function:
                fc["name"] = tmp + " " + hex(f["from"])
                items.append(fc["name"])
                fc["comment"] = ""
                fc["from"] = hex(f["from"])
                if "_id" in fc:
                    del fc["_id"]
                func_db.insert_one(fc)

    return items


class dynamic_thread(QtCore.QThread):
    textSignal = QtCore.pyqtSignal(str)
    stopSignal = QtCore.pyqtSignal()

    def __init__(self, rlocal):
        super(dynamic_thread, self).__init__()
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
                byteStr = byteStr + str(hex(messageArr[i]))[2:]

            if "ffffffff" not in byteStr:
                self.textSignal.emit(byteStr)
        self.stopSignal.emit()
