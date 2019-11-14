from PyQt5 import QtCore, QtWidgets, QtGui
import base64
from model import Analysis, DBConnection, Plugin, r2Connection
from model.Singleton import Singleton
from view.pop.CommentDialog import CommentDialog
from view.pop.OutputFieldDialog import OutputFieldDialog
from . import poi_formatter

class AnalysisTabController:

    def __init__(self, analysisTab):
        self.analysisTab = analysisTab
        self.analysisTab.poi_content_area_textEdit.setStyleSheet('')

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
        self.analysisTab.search_bar_lineEdit.textChanged.connect(
            lambda x: self.search_filtered_pois(self.analysisTab.search_bar_lineEdit.text()))

    def establish_calls(self):
        self.analysisTab.terminal_output_textEdit.setReadOnly(True)
        self.set_plugins()

    def set_plugins(self):
        for pl in Plugin.get_installed_plugins():
            self.analysisTab.plugin_comboBox.addItem(pl)

    def set_item(self, text, type):
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(type)
        return item

    def static_ran(self):
        if Singleton.get_project() == "BEAT":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
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
            msg = QtWidgets.QMessageBox()
            msg.setText(str(e))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
        QtWidgets.QApplication.restoreOverrideCursor()

    def poi_comboBox_change(self, text):
        if Singleton.get_project() == "BEAT":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        self.analysisTab.poi_listWidget.clear()

        project_db = DBConnection.get_collection(Singleton.get_project())

        if text == "Functions":
            project_info = project_db["functions"]
            cursor = project_info.find()
            for db in cursor:
                item = self.set_item(db["name"], "Functions")
                self.analysisTab.poi_listWidget.addItem(item)
        elif text == "Strings":
            project_info = project_db["string"]
            cursor = project_info.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.analysisTab.poi_listWidget.addItem(item)

        elif text == "All":
            project_info = project_db["functions"]
            cursor = project_info.find()
            for db in cursor:
                item = self.set_item(db["name"], "Functions")
                self.analysisTab.poi_listWidget.addItem(item)
            project_info = project_db["string"]
            cursor = project_info.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
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
            #y = str(value)
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
        pop_up = OutputFieldDialog(self)
        text = pop_up.exec_()
        print(text)

    def terminal(self, text):
        if text is not "":
            last_text = self.analysisTab.terminal_output_textEdit.toPlainText()
            self.analysisTab.terminal_output_textEdit.setText(last_text + text + "\n")
            self.analysisTab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)


    def breakpoint_check(self):

        text, ok_pressed = QtWidgets.QInputDialog.getText(self.analysisTab, "Dynamic Analysis", "Args to pass:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if ok_pressed:
            pois_checked = []
            global r2
            r2 = r2Connection.Open(Singleton.get_path())
            self.terminal(r2.cmd("aaa"))
            self.terminal(r2.cmd("doo %s" %text))

            for i in range(self.analysisTab.poi_listWidget.count()):
                item = self.analysisTab.poi_listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    pois_checked.append(item)
            for ix in pois_checked:
                value = DBConnection.search_by_item(ix)
                oc = value["ocurrence"]
                for o in oc:
                    r2breakpoint = 'db ' + o

                    self.terminal(r2.cmd(r2breakpoint))

    def stepup(self):
        try:
            self.terminal(r2.cmd("dc"))
            self.terminal(r2.cmd("dso"))
        except NameError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Dynamic Analysis")
            msg.setText("Run a dynamic analysis first")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return