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
        text = string["string"]
        textDecoded = base64.b64decode(text)
        for i in str_plg:
            if i.upper() in textDecoded.decode().upper():
                x = rlocal.cmdj("axtj %s" % string["vaddr"])
                tmp = textDecoded.decode()
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
                fc["runs"] = []
                fc["from"] = hex(f["from"])
                if "_id" in fc:
                    del fc["_id"]
                func_db.insert_one(fc)

    return items


class dynamic_thread(QtCore.QThread):
    textSignal = QtCore.pyqtSignal(str)
    listSignal = QtCore.pyqtSignal(dict)
    stopSignal = QtCore.pyqtSignal()

    def __init__(self, rlocal, pois):
        super(dynamic_thread, self).__init__()
        self.rlocal = rlocal
        self.pois = pois

    def run(self):
       for poi in self.pois:
           fr = poi["from"]
           r2Breakpoint = 'db '+fr
           self.rlocal.cmd(r2Breakpoint)

           x = self.rlocal.cmd("dc")
           poi["rtnPara"] =  self.checkPara()
           if "Cannot continue, run ood?" in x:
               break
           self.textSignal.emit(x)
           y = self.rlocal.cmd("dso")
           self.textSignal.emit(y)

           messageAddr = self.rlocal.cmd("dr rsi")
           lookInBuff = "pxj @" + messageAddr
           messageArr = self.rlocal.cmdj(lookInBuff)
           byteStr = ""

           for i in range(len(messageArr)):
               if messageArr[i] == 0:
                   break
               byteStr = byteStr + str(hex(messageArr[i]))[2:]

           if "ffffffff" not in byteStr:
               poi["rtnFnc"] = byteStr
           else:
               poi["rtnFnc"] = "No Value"
           self.listSignal.emit(poi)

    def stop(self):
        self.rlocal.quit()

    def checkPara(self):
        self.rlocal.cmd("s")
        i=0
        ValPara = []
        seen = []
        while True:
            i+=1
            code = self.rlocal.cmdj('pdj '+ str(-i))
            if code[0]['type'] == 'mov' or code[0]['type'] == 'lea':
                split_cmd = code[0]['opcode'].replace(',', '').split()
                if len(split_cmd) < 2:
                    pass
                elif not (split_cmd[1] in seen):
                    if split_cmd[1] == 'qword':
                        x = " ".join(split_cmd[2:-1]).replace('[', '').replace(']', '')
                        value = self.rlocal.cmd('dr '+x)

                    elif split_cmd[1].__contains__("word"):
                        pass
                    else:
                        x = split_cmd[1]
                        value = self.rlocal.cmd('dr '+x)
                        seen.append(split_cmd[1])
                ValPara.append(value)
            else:
                break
        return ValPara
