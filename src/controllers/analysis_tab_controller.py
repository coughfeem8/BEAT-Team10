from PyQt5 import QtCore, QtWidgets
import pop
import base64
import r2pipe
from model import analysis, dbconnection, plugin
from model.singleton import Singleton


class analysis_tab_controller:

    def __init__(self, analysisTab):
        self.analysisTab = analysisTab

    def establish_connections(self):
        self.analysisTab.static_run_button.clicked.connect(self.static_ran)
        self.analysisTab.poi_comboBox.currentIndexChanged.connect(
            lambda x: self.poi_comboBox_change(text=self.analysisTab.poi_comboBox.currentText()))
        self.analysisTab.poi_listWidget.itemClicked.connect(
            lambda x: self.detailed_poi(self.analysisTab.poi_listWidget.currentItem()))
        self.analysisTab.dynamic_run_button.clicked.connect(self.breakpoint_check)
        self.analysisTab.comment_PushButton.clicked.connect(self.open_comment)
        self.analysisTab.output_PushButton.clicked.connect(self.open_output)

    def establish_calls(self):
        self.setPlugins()

    def setPlugins(self):
        for pl in plugin.getInstalledPlugins():
            self.analysisTab.plugin_comboBox.addItem(pl)

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

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.analysisTab.poi_listWidget.clear()
        rlocal = analysis.staticAll(Singleton.getPath())
        try:
            print("were here")
            if self.analysisTab.poi_comboBox.currentText() == "All":
                print("were in all now")
                strings = analysis.staticStrings(rlocal,self.analysisTab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysisTab.poi_listWidget.addItem(item)

                functions = analysis.staticFunctions(rlocal,self.analysisTab.plugin_comboBox.currentText())
                print(functions)
                print("functions apparently printed")
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    print(item.text())
                    print("Text test")
                    self.analysisTab.poi_listWidget.addItem(item)

            elif self.analysisTab.poi_comboBox.currentText() == "Functions":

                functions = analysis.staticFunctions(rlocal,self.analysisTab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    print(item.text())
                    self.analysisTab.poi_listWidget.addItem(item)

            elif self.analysisTab.poi_comboBox.currentText() == "Strings":

                strings = analysis.staticStrings(rlocal,self.analysisTab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysisTab.poi_listWidget.addItem(item)

        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText(str(e))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
        QtWidgets.QApplication.restoreOverrideCursor()

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

        projectDb = dbconnection.getCollection(s)

        if text == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["name"], "Functions")
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
                item = self.set_item(db["name"], "Functions")
                self.analysisTab.poi_listWidget.addItem(item)
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.analysisTab.poi_listWidget.addItem(item)

    def detailed_poi(self, item):
        s = Singleton.getProject()
        projectDb = dbconnection.getCollection(s)
        value = None
        if item.toolTip() == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find_one({"name": item.text()})
            if cursor is not None:
                value = {'name':cursor["name"], 'signature':cursor["signature"],'varaddress':hex(cursor["offset"]), 'ocurrence':cursor["ocurrence"], 'comment':cursor["comment"]}
        elif item.toolTip() == "Strings":
            projInfo = projectDb["string"]
            text = base64.b64encode(item.text().encode())
            cursor = projInfo.find_one({"string": text.decode()})
            if cursor is not None:
                value = {'string':text,'varaddress':hex(cursor["vaddr"]), 'ocurrence':cursor["ocurrence"], 'comment':cursor["comment"]}
        if value is not None:
            y = str(value)
            self.analysisTab.poi_content_area_textEdit.setPlainText(y)

    def open_comment(self):

        item = self.analysisTab.poi_listWidget.currentItem()
        s = Singleton.getProject()
        projectDB = dbconnection.getCollection(s)
        value = None
        if item.toolTip() == "Functions":
            dbInfo = projectDB["functions"]
            cursor = dbInfo.find_one({"name": item.text()})
            if cursor is not  None:
                value = cursor["_id"]
                cmt = cursor["comment"]
        elif item.toolTip() == "Strings":
            dbInfo = projectDB["string"]
            text = base64.b64encode(item.text().encode())
            cursor = dbInfo.find_one({"string": text.decode()})
            if cursor is not None:
                value = cursor["_id"]
                cmt = cursor["comment"]
        if value is not None:
            if cmt is None:
                cmt = ""
            popUp = pop.commentDialog(self.analysisTab, cmt)
            comm = popUp.exec_()
            index = {"_id": value}
            newValue = {"$set": {"comment": comm}}
            dbInfo.update_one(index, newValue)
            self.detailed_poi(item)

    def open_output(self):
        popUp = pop.outputFieldDialog(self)
        text = popUp.exec_()
        print(text)

    def breakpoint_check(self):
        for i in range(self.analysisTab.poi_listWidget.count()):
            item = self.analysisTab.poi_listWidget.item(i)
            print(f"{i} {item.text()} {item.checkState()}")
