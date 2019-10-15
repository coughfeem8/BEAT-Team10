from PyQt5 import QtCore, QtGui, QtWidgets
import tab1, tab2, tab3, tab4, tab5
import analysis
from singleton import Singleton
import pymongo
import base64


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("BEAT")
        MainWindow.resize(804, 615)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        MainWindow.setWindowTitle("BEAT")
        s = Singleton()
        s.setProject("BEAT")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 794, 605))
        self.tabWidget.setObjectName("tabWidget")

        self.ProjectTab = tab1.Tab1(self, MainWindow)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = tab2.Tab2(self, self)
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = tab3.Tab3(self, self)
        self.tabWidget.addTab(self.pluginTab, "")

        self.pointsOfInterestTab = tab4.Tab4(self, self)
        self.tabWidget.addTab(self.pointsOfInterestTab, "")

        self.documentationTab = tab5.Tab5(self, self)
        self.tabWidget.addTab(self.documentationTab, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProjectTab), _translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pluginTab), _translate("MainWindow", "Plugin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsOfInterestTab),
                                  _translate("MainWindow", "Points of Interest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documentationTab),
                                  _translate("MainWindow", "Documentation"))
        self.establish_connections(MainWindow)

    def establish_connections(self, MainWindow):
        self.analysisTab.static_run_button.clicked.connect(self.static_ran)

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

    def set_pois(self, projectDb, functions, variables, rec_structs, sent_structs, strings, imports):
        projInfo = projectDb["functions"]
        cursor = projInfo.find()
        for db in cursor:
            item = self.analysisTab.set_item(db["signature"], "Functions")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb['variables']
        coursor = projInfo.find()
        for db in coursor:
            item = self.analysisTab.set_item("%s %s" % (db["type"], db["name"]), "Variables")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb["imports"]
        cursor = projInfo.find()
        for db in cursor:
            item = self.analysisTab.set_item(db["name"] + " " + db["type"], "Imports")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb["structures"]
        cursor = projInfo.find()
        for db in cursor:
            insert_send = {"address": hex(db["from"]), "opcode": db["opcode"],
                           "calling_function": db["fcn_name"]}
            item = self.analysisTab.set_item("send " + insert_send["calling_function"] + " " + insert_send["address"],
                                 "Structs")
            self.analysisTab.poi_listWidget.addItem(item)
        projInfo = projectDb["string"]
        cursor = projInfo.find()
        for db in cursor:
            text = base64.b64decode(db["string"])
            item = self.analysisTab.set_item(text.decode(), "Strings")
            self.analysisTab.poi_listWidget.addItem(item)
        """
        elif text == "All":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["signature"], "Functions")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["variables"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item("%s %s" % (db["type"], db["name"]), "Variables")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:
                insert_send = {"address": hex(db["from"]), "opcode": db["opcode"],
                               "calling_function": db["fcn_name"]}
                item = self.set_item("send " + insert_send["calling_function"] + " " + insert_send["address"],
                                     "Structs")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["name"] + " " + db["type"], "Imports")
                self.poi_listWidget.addItem(item)
        """


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
