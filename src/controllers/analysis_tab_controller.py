from PyQt5 import QtCore, QtWidgets, QtGui
from view import pop
import base64
from model import analysis, dbconnection, plugin, r2connection, test
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
        self.analysisTab.dynamic_stop_button.clicked.connect(self.stepup)

    def establish_calls(self):
        self.analysisTab.terminal_output_textEdit.setReadOnly(True)
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
            if self.analysisTab.poi_comboBox.currentText() == "All":

                strings = analysis.staticStrings(rlocal,self.analysisTab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysisTab.poi_listWidget.addItem(item)

                functions = analysis.staticFunctions(rlocal,self.analysisTab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    self.analysisTab.poi_listWidget.addItem(item)

            elif self.analysisTab.poi_comboBox.currentText() == "Functions":

                functions = analysis.staticFunctions(rlocal,self.analysisTab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
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
        value = dbconnection.searchByItem(item)
        if value is not None:
            del value["_id"]
            y = str(value)
            self.analysisTab.poi_content_area_textEdit.setPlainText(y)

    def open_comment(self):
        s = Singleton.getProject()
        item = self.analysisTab.poi_listWidget.currentItem()
        value = dbconnection.searchByItem(item)
        projectDb = dbconnection.getCollection(s)
        if item.toolTip() == "Functions":
            dbInfo = projectDb["function"]
        elif item.toolTip() == "Strings":
            dbInfo = projectDb["string"]
        if value is not None:
            id = value["_id"]
            cmt = value["comment"]
            if cmt is None:
                cmt = ""
            popUp = pop.commentDialog(self.analysisTab, cmt)
            comm = popUp.exec_()
            index = {"_id": id}
            newValue = {"$set": {"comment": comm}}
            dbInfo.update_one(index, newValue)
            self.detailed_poi(item)

    def open_output(self):
        popUp = pop.outputFieldDialog(self)
        text = popUp.exec_()
        print(text)

    def terminal(self, text):
        if text is not "":
            lastText = self.analysisTab.terminal_output_textEdit.toPlainText()
            self.analysisTab.terminal_output_textEdit.setText(lastText + text + "\n")
            self.analysisTab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)


    def breakpoint_check(self):

        text, okPressed = QtWidgets.QInputDialog.getText(self.analysisTab, "Dynamic Analysis", "Args to pass:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if okPressed:
            poisChecked = []
            r2 = r2connection.open(Singleton.getPath())
            self.terminal(r2.cmd("aaa"))
            self.terminal(r2.cmd("doo %s" %text))

            for i in range(self.analysisTab.poi_listWidget.count()):
                item = self.analysisTab.poi_listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    poisChecked.append(item)
            for ix in poisChecked:
                value = dbconnection.searchByItem(ix)
                oc = value["ocurrence"]
                for o in oc:
                    r2breakpoint = 'db ' + o

                    self.terminal(r2.cmd(r2breakpoint))

            global thread
            thread = test.AThread(rlocal=r2,terminal=self.analysisTab)
            thread.start()

    def stepup(self):
        try:
            thread.terminate()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Dynamic Analysis")
            msg.setText(str(e))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
