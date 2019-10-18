from PyQt5 import QtCore, QtGui, QtWidgets
import pop
import pymongo
import base64
import analysis
from singleton import Singleton


class analysis_tab_controller():

    def __init__(self, analysisTab):
        self.analysisTab = analysisTab

    def establish_connections(self):
        self.analysisTab.static_run_button.clicked.connect(self.static_ran)
        self.analysisTab.poi_comboBox.currentIndexChanged.connect(
            lambda x: self.poi_comboBox_change(text=self.analysisTab.poi_comboBox.currentText()))
        self.analysisTab.dynamic_run_button.clicked.connect(self.breakpoint_check)
        self.analysisTab.comment_PushButton.clicked.connect(self.open_comment)
        self.analysisTab.analysis_PushButton.clicked.connect(self.open_analysis)
        self.analysisTab.output_PushButton.clicked.connect(self.open_output)

    def set_item(self, text, type):
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(type)
        return item

    def static_ran(self):
        s = Singleton.getProject()
        if (s == "BEAT"):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]
        projInfo = projectDb["projectInfo"]
        cursor = projInfo.find()
        binary_file = ""

        for db in cursor:
            binary_file = db['BnyFilePath']

        functions, variables, rec_structs, sent_structs, strings, imports = analysis.static_analysis(binary_file)

        # insert functions
        if projectDb["functions"]:
            projectDb.drop_collection("functions")
        fnctDB = projectDb["functions"]
        for fc in functions:
            insert_info = {'offset': fc["offset"], 'name': fc["name"], 'size': fc["size"], 'signature': fc["signature"]}
            fnctDB.insert_one(insert_info)

        # insert variables
        if projectDb["variables"]:
            projectDb.drop_collection("variables")
        varDB = projectDb["variables"]
        variables = variables[:-1]
        for variable in variables:
            var = variable.split()
            if var[var.index('=') + 1] == ':':
                var.insert(var.index('=') + 1, 0)
            insert_info = {"type": var[0], "name": var[1], "value": var[3], "register": var[5], "location": var[7]}
        varDB.insert_one(insert_info)

        # insert structs
        if projectDb["structures"]:
            projectDb.drop_collection("structures")
        strucDB = projectDb["structures"]
        for rec in rec_structs:
            insert_recv = {"address": hex(rec["from"]), "opcode": rec["opcode"], "calling_function": rec["fcn_name"]}
            strucDB.insert_one(insert_recv)

        for send in sent_structs:
            insert_send = {"address": hex(send["from"]), "opcode": send["opcode"], "calling_function": send["fcn_name"]}
            strucDB.insert_one(insert_send)

        # insert Strings
        if projectDb["string"]:
            projectDb.drop_collection("string")
        strDB = projectDb["string"]
        for string in strings:
            if string["section"] == '.rodata':
                text = base64.b64decode(string["string"])
                strDB.insert_one(string)

        # insert DLLs
        if projectDb["imports"]:
            projectDb.drop_collection("imports")
        impDB = projectDb["imports"]
        for dl in imports:
            impDB.insert_one(dl)

        self.set_pois(projectDb, functions, variables, rec_structs, sent_structs, strings, imports)
        self.analysisTab.poi_listWidget.itemClicked.connect(
            lambda x: self.detailed_poi(self.analysisTab.poi_listWidget.currentItem()))

    def set_pois(self, projectDb, functions, variables, rec_structs, sent_structs, strings, imports):
        projInfo = projectDb["functions"]
        cursor = projInfo.find()
        for db in cursor:
            item = self.set_item(db["signature"], "Functions")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb['variables']
        coursor = projInfo.find()
        for db in coursor:
            item = self.set_item("%s %s" % (db["type"], db["name"]), "Variables")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb["imports"]
        cursor = projInfo.find()
        for db in cursor:
            item = self.set_item(db["name"] + " " + db["type"], "Imports")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb["structures"]
        cursor = projInfo.find()
        for db in cursor:
            insert_send = {"address": db["address"], "opcode": db["opcode"],
                           "calling_function": db["calling_function"]}
            item = self.set_item("send " + insert_send["calling_function"] + " " + insert_send["address"],
                                             "Structs")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb["string"]
        cursor = projInfo.find()
        for db in cursor:
            text = base64.b64decode(db["string"])
            item = self.set_item(text.decode(), "Strings")
            self.analysisTab.poi_listWidget.addItem(item)

    def poi_comboBox_change(self, text):
        s = Singleton.getProject()
        if s == "BEAT":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        self.analysisTab.poi_listWidget.clear()

        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]

        if text == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["signature"], "Functions")
                self.analysisTab.poi_listWidget.addItem(item)
        elif text == "Variables":
            projInfo = projectDb['variables']
            coursor = projInfo.find()
            for db in coursor:
                item = self.set_item("%s %s" % (db["type"], db["name"]), "Variables")
                self.analysisTab.poi_listWidget.addItem(item)
        elif text == "DLLs":
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["name"] + " " + db["type"], "Imports")
                self.analysisTab.poi_listWidget.addItem(item)
        elif text == "Structs":
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:
                insert_send = {"address": hex(db["from"]), "opcode": db["opcode"],
                               "calling_function": db["fcn_name"]}
                item = self.set_item(
                    "send " + insert_send["calling_function"] + " " + insert_send["address"],
                    "Structs")
                self.analysisTab.poi_listWidget.addItem(item)
        elif text == "Strings":
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.analysisTab.poi_listWidget.addItem(item)

        elif text == "All":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.analysisTab.set_item(db["signature"], "Functions")
                self.analysisTab.poi_listWidget.addItem(item)
            projInfo = projectDb["variables"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item("%s %s" % (db["type"], db["name"]), "Variables")
                self.analysisTab.poi_listWidget.addItem(item)
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:
                insert_send = {"address": db["address"], "opcode": db["opcode"],
                               "calling_function": db["calling_function"]}
                item = self.set_item(
                    "send " + insert_send["calling_function"] + " " + insert_send["address"],
                    "Structs")
                self.analysisTab.poi_listWidget.addItem(item)
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.analysisTab.poi_listWidget.addItem(item)
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["name"] + " " + db["type"], "Imports")
                self.analysisTab.poi_listWidget.addItem(item)

    def detailed_poi(self, item):
        s = Singleton.getProject()
        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]

        lastText = self.analysisTab.poi_content_area_textEdit.toPlainText()

        if item.toolTip() == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find_one({"signature": item.text()})
        elif item.toolTip() == "Variables":
            projInfo = projectDb["variables"]
            var = item.text().split()
            cursor = projInfo.find_one({"name": var[1]})
        elif item.toolTip() == "Imports":
            projInfo = projectDb["imports"]
            text = item.text().split()
            cursor = projInfo.find_one({"name": text[0]})
        elif item.toolTip() == "Strings":
            projInfo = projectDb["string"]
            cursor = projInfo.find_one({"string": item.text()})
        elif item.toolTip() == "Structs":
            projInfo = projectDb["structures"]
            text = item.text().split()
            cursor = projInfo.find_one({"from": int(text[2], 0)})
        del cursor['_id']
        y = str(cursor)
        lastText = lastText.replace("\n" + y, ' ')
        self.analysisTab.poi_content_area_textEdit.setPlainText(y)

    def open_comment(self):
        popUp = pop.commentDialog(self)
        text = popUp.exec_()
        print(text)

    def open_analysis(self):
        popUp = pop.analysisResultDialog(self)
        text = popUp.exec_()
        print(text)

    def open_output(self):
        popUp = pop.outputFieldDialog(self)
        text = popUp.exec_()
        print(text)

    def breakpoint_check(self):
        for i in range(self.analysisTab.poi_listWidget.count()):
            item = self.analysisTab.poi_listWidget.item(i)
            print(f"{i} {item.text()} {item.checkState()}")
