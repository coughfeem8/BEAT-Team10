from PyQt5 import QtCore, QtWidgets, QtGui
import base64
from model import Analysis, DBConnection, Plugin, r2Connection
from model.Singleton import Singleton
from view.pop.ErrorDialog import ErrorDialog
from view.pop.CommentDialog import CommentDialog
from view.pop.OutputFieldDialog import OutputFieldDialog
from . import poi_formatter

class AnalysisTabController:

    def __init__(self, analysisTab, main):
        self.analysisTab = analysisTab
        self.analysisTab.poi_content_area_textEdit.setStyleSheet('')
        self.main = main

    def establish_connections(self):
        self.analysisTab.static_run_button.clicked.connect(self.static)
        self.analysisTab.poi_comboBox.currentIndexChanged.connect(
            lambda x: self.poi_comboBox_change(text=self.analysisTab.poi_comboBox.currentText()))
        self.analysisTab.poi_listWidget.itemClicked.connect(
            lambda x: self.detailed_poi(self.analysisTab.poi_listWidget.currentItem()))
        self.analysisTab.dynamic_run_button.clicked.connect(self.dynamic)
        self.analysisTab.comment_PushButton.clicked.connect(self.open_comment)
        self.analysisTab.output_PushButton.clicked.connect(self.open_output)
        self.analysisTab.dynamic_stop_button.clicked.connect(self.stop)
        self.analysisTab.search_bar_lineEdit.textChanged.connect(
            lambda x: self.search_filtered_pois(self.analysisTab.search_bar_lineEdit.text()))

    def establish_calls(self):
        self.analysisTab.terminal_output_textEdit.setReadOnly(True)
        self.set_plugins()

    def set_plugins(self):
        self.analysisTab.plugin_comboBox.clear()
        for pl in Plugin.get_installed_plugins():
            self.analysisTab.plugin_comboBox.addItem(pl)

    def set_item(self, text, type):
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(type)
        return item

    def static(self):
        s = Singleton.get_project()
        if (s == "BEAT"):
            x = ErrorDialog(self.analysisTab, "Please select a project", "Static Analysis Error")
            x.exec_()
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.analysisTab.poi_listWidget.clear()
        rlocal = Analysis.static_all(Singleton.get_path())
        try:
            if self.analysisTab.poi_comboBox.currentText() == "All":

                strings = Analysis.static_strings(rlocal, self.analysisTab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysisTab.poi_listWidget.addItem(item)

                functions = Analysis.static_functions(rlocal, self.analysisTab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    self.analysisTab.poi_listWidget.addItem(item)

            elif self.analysisTab.poi_comboBox.currentText() == "Functions":

                functions = Analysis.static_functions(rlocal, self.analysisTab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    self.analysisTab.poi_listWidget.addItem(item)

            elif self.analysisTab.poi_comboBox.currentText() == "Strings":

                strings = Analysis.static_strings(rlocal, self.analysisTab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysisTab.poi_listWidget.addItem(item)

        except Exception as e:
            x = ErrorDialog(self.analysisTab, str(e), "Static Analysis Error")
            x.exec_()
        rlocal.quit()
        QtWidgets.QApplication.restoreOverrideCursor()



    def poi_comboBox_change(self, text):
        s = Singleton.get_project()
        if s == "BEAT":
            msg = ErrorDialog(self.analysisTab, "Please select a project first", "Static Analysis Error")
            msg.exec_()
            return

        self.analysisTab.poi_listWidget.clear()

        projectDb = DBConnection.get_collection(s)

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
                text = db["string"]
                item = self.set_item(text, "Strings")
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
                text = db["string"]
                item = self.set_item(text, "Strings")
                self.analysisTab.poi_listWidget.addItem(item)

    def search_filtered_pois(self, text):
        if len(text) is not 0:
            search_result = self.analysisTab.poi_listWidget.findItems(text, QtCore.Qt.MatchContains)
            for item in range(self.analysisTab.poi_listWidget.count()):
                self.analysisTab.poi_listWidget.item(item).setHidden(True)
            for item in search_result:
                item.setHidden(False)
        else:
            for item in range(self.analysisTab.poi_listWidget.count()):
                self.analysisTab.poi_listWidget.item(item).setHidden(False)

    def detailed_poi(self, item):
        value = DBConnection.search_by_item(item)
        if value is not None:
            del value["_id"]
            y = value
            self.analysisTab.poi_content_area_textEdit.setHtml(poi_formatter.format(y))

    def open_comment(self):
        item = self.analysisTab.poi_listWidget.currentItem()
        value = DBConnection.search_by_item(item)
        project_db = DBConnection.get_collection(Singleton.get_project())
        if item.toolTip() == "Functions":
            db_info = project_db["function"]
        elif item.toolTip() == "Strings":
            db_info = project_db["string"]
        if value is not None:
            id = value["_id"]
            cmt = value["comment"]
            if cmt is None:
                cmt = ""
            pop_up = CommentDialog(self.analysisTab, cmt)
            comm = pop_up.exec_()
            index = {"_id": id}
            new_value = {"$set": {"comment": comm}}
            db_info.update_one(index, new_value)
            self.detailed_poi(item)
            new_font = QtGui.QFont()
            new_font.setBold(True)
            item.setFont(new_font)

    def open_output(self):
        pop_up = OutputFieldDialog(self.analysisTab)
        text = pop_up.exec_()
        print(text)

    def terminal(self, text):
        if text is not "":
            last_text = self.analysisTab.terminal_output_textEdit.toPlainText()
            self.analysisTab.terminal_output_textEdit.setText(last_text + text + "\n")
            self.analysisTab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)


    def dynamic(self):

        text, okPressed = QtWidgets.QInputDialog.getText(self.analysisTab, "Dynamic Analysis", "Args to pass:",
                                                         QtWidgets.QLineEdit.Normal, "")

        if okPressed:
            poisChecked = []

            r2 = Analysis.static_all(Singleton.get_path())
            self.terminal(r2.cmd("doo %s" % text))

            for i in range(self.analysisTab.poi_listWidget.count()):
                item = self.analysisTab.poi_listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    if item.toolTip() == "Functions":
                        value = DBConnection.search_by_item(item)
                        poi = {"name":item.text(),"from":value["from"],"type":item.toolTip(),"rtnPara":[],"rtnFnc":""}
                        poisChecked.append(poi)

            sort = sorted(poisChecked, key= lambda i: i["from"])

            global thread
            self.main.setWindowTitle("BEAT | Running " + Singleton.get_project())
            thread = Analysis.dynamic_thread(rlocal=r2, pois=sort)
            thread.textSignal.connect(lambda x: self.terminal(x))
            thread.stopSignal.connect(self.setStopTitle)
            thread.listSignal.connect(lambda x: self.print(x))
            thread.start()

    def print(self, text):
        print(text)

    def stop(self):
        try:
            thread.terminate()
            self.setStopTitle()
        except:
            x = ErrorDialog(self.analysisTab,"Run a dynamic analysis first", "Dynamic Analysis Error")
            x.exec_()

    def setStopTitle(self):
        self.main.setWindowTitle("BEAT | "+Singleton.get_project())