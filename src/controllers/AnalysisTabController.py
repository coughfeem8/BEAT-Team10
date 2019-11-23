from PyQt5 import QtCore, QtWidgets, QtGui
import subprocess

import model.Analysis.DynamicThread
import model.Analysis.StaticAnalysis
from model import DBConnection, Plugin
from model.Singleton import Singleton
from view.pop.ErrorDialog import ErrorDialog
from view.pop.CommentDialog import CommentDialog


class AnalysisTabController:

    def __init__(self, analysis_tab, main):
        self.analysis_tab = analysis_tab
        self.analysis_tab.poi_content_area_textEdit.setStyleSheet('')
        self.main = main
        self.run = 0

    def establish_connections(self):
        self.analysis_tab.static_run_button.clicked.connect(self.static)
        self.analysis_tab.poi_comboBox.currentIndexChanged.connect(
            lambda x: self.poi_comboBox_change(text=self.analysis_tab.poi_comboBox.currentText()))
        self.analysis_tab.poi_listWidget.itemClicked.connect(
            lambda x: self.detailed_poi(self.analysis_tab.poi_listWidget.currentItem()))
        self.analysis_tab.dynamic_run_button.clicked.connect(self.dynamic)
        self.analysis_tab.comment_PushButton.clicked.connect(self.open_comment)
        self.analysis_tab.output_PushButton.clicked.connect(self.open_output)
        self.analysis_tab.dynamic_stop_button.clicked.connect(self.stop)
        self.analysis_tab.search_bar_lineEdit.textChanged.connect(
            lambda x: self.search_filtered_pois(self.analysis_tab.search_bar_lineEdit.text()))

    def establish_calls(self):
        self.analysis_tab.terminal_output_textEdit.setReadOnly(True)
        self.set_plugins()

    def set_plugins(self):
        self.analysis_tab.plugin_comboBox.clear()
        for pl in Plugin.get_installed_plugins():
            self.analysis_tab.plugin_comboBox.addItem(pl)

    def set_item(self, text, poi_type):
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(poi_type)
        return item

    def static(self):
        s = Singleton.get_project()
        if s == "BEAT":
            x = ErrorDialog(self.analysis_tab, "Please select a project", "Static Analysis Error")
            x.exec_()
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.analysis_tab.poi_listWidget.clear()
        rlocal = model.Analysis.StaticAnalysis.static_all(Singleton.get_path())
        try:
            if self.analysis_tab.poi_comboBox.currentText() == "All":

                strings = model.Analysis.StaticAnalysis.static_strings(rlocal, self.analysis_tab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysis_tab.poi_listWidget.addItem(item)

                functions = model.Analysis.StaticAnalysis.static_functions(rlocal, self.analysis_tab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    self.analysis_tab.poi_listWidget.addItem(item)

            elif self.analysis_tab.poi_comboBox.currentText() == "Functions":

                functions = model.Analysis.StaticAnalysis.static_functions(rlocal, self.analysis_tab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    self.analysis_tab.poi_listWidget.addItem(item)

            elif self.analysis_tab.poi_comboBox.currentText() == "Strings":

                strings = model.Analysis.StaticAnalysis.static_strings(rlocal, self.analysis_tab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    self.analysis_tab.poi_listWidget.addItem(item)

        except Exception as e:
            x = ErrorDialog(self.analysis_tab, str(e), "Static Analysis Error")
            x.exec_()
        rlocal.quit()
        QtWidgets.QApplication.restoreOverrideCursor()

    def poi_comboBox_change(self, text):
        s = Singleton.get_project()
        if s == "BEAT":
            msg = ErrorDialog(self.analysis_tab, "Please select a project first", "Static Analysis Error")
            msg.exec_()
            return

        self.analysis_tab.poi_listWidget.clear()

        project_db = DBConnection.get_collection(s)

        if text == "Functions":
            project_info = project_db["functions"]
            cursor = project_info.find()
            for db in cursor:
                item = self.set_item(db["name"], "Functions")
                self.analysis_tab.poi_listWidget.addItem(item)
        elif text == "Strings":
            project_info = project_db["string"]
            cursor = project_info.find()
            for db in cursor:
                text = db["string"]
                item = self.set_item(text, "Strings")
                self.analysis_tab.poi_listWidget.addItem(item)

        elif text == "All":
            project_info = project_db["functions"]
            cursor = project_info.find()
            for db in cursor:
                item = self.set_item(db["name"], "Functions")
                self.analysis_tab.poi_listWidget.addItem(item)
            project_info = project_db["string"]
            cursor = project_info.find()
            for db in cursor:
                text = db["string"]
                item = self.set_item(text, "Strings")
                self.analysis_tab.poi_listWidget.addItem(item)

    def search_filtered_pois(self, text):
        if len(text) is not 0:
            search_result = self.analysis_tab.poi_listWidget.findItems(text, QtCore.Qt.MatchContains)
            for item in range(self.analysis_tab.poi_listWidget.count()):
                self.analysis_tab.poi_listWidget.item(item).setHidden(True)
            for item in search_result:
                item.setHidden(False)
        else:
            for item in range(self.analysis_tab.poi_listWidget.count()):
                self.analysis_tab.poi_listWidget.item(item).setHidden(False)

    def detailed_poi(self, item):
        value = DBConnection.search_by_item(item)
        if value is not None:
            del value["_id"]
            y = str(value)
            self.analysis_tab.poi_content_area_textEdit.setText(y)

    def open_comment(self):
        item = self.analysis_tab.poi_listWidget.currentItem()
        value = DBConnection.search_by_item(item)
        project_db = DBConnection.get_collection(Singleton.get_project())
        if item.toolTip() == "Functions":
            db_info = project_db["functions"]
        elif item.toolTip() == "Strings":
            db_info = project_db["string"]
        if value is not None:
            id = value["_id"]
            cmt = value["comment"]
            if cmt is None:
                cmt = ""
            pop_up = CommentDialog(self.analysis_tab, cmt)
            comm = pop_up.exec_()
            index = {"_id": id}
            new_value = {"$set": {"comment": comm}}
            db_info.update_one(index, new_value)
            self.detailed_poi(item)
            new_font = QtGui.QFont()
            new_font.setBold(True)
            item.setFont(new_font)

    def open_output(self):
        try:
            plugin = Plugin.get_file(self.analysis_tab.plugin_comboBox.currentText())
            cmd = ["python3", plugin]
            pois = []
            for i in range(self.analysis_tab.poi_listWidget.count()):
                item = self.analysis_tab.poi_listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    value = DBConnection.search_by_item(item)
                    out = Plugin.get_output(item.text(), self.analysis_tab.plugin_comboBox.currentText())
                    poi = {"name": item.text(), "from": value["from"], "out": out}
                    pois.append(poi)
            sort = sorted(pois, key=lambda i: i["from"])
            for s in sort:
                cmd.append(str(s))
            # print(cmd)
            subprocess.check_call(cmd)
            # proc.w
            x = ErrorDialog(self.analysis_tab, "Finished creating output", "Output")
            x.exec_()
        except subprocess.CalledProcessError as e:
            text = ""
            if e.returncode == 1:
                text = f"Error executing {plugin} file"
            elif e.returncode == 2:
                text = f"{plugin} file not found"

            x = ErrorDialog(self.analysis_tab, text, "Error in Output")
            x.exec_()
        except Exception as e:
            x = ErrorDialog(self.analysis_tab, str(e), "Error in Output")
            x.exec_()

    def terminal(self, text):
        if text is not "":
            last_text = self.analysis_tab.terminal_output_textEdit.toPlainText()
            self.analysis_tab.terminal_output_textEdit.setText(last_text + text + "\n")
            self.analysis_tab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)

    def dynamic(self):

        text, ok_pressed = QtWidgets.QInputDialog.getText(self.analysis_tab, "Dynamic Analysis", "Args to pass:",
                                                          QtWidgets.QLineEdit.Normal, "")

        if ok_pressed:
            self.run += 1
            pois_checked = []

            r2 = model.Analysis.StaticAnalysis.static_all(Singleton.get_path())
            self.terminal(r2.cmd("doo %s" % text))

            for i in range(self.analysis_tab.poi_listWidget.count()):
                item = self.analysis_tab.poi_listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    if item.toolTip() == "Functions":
                        value = DBConnection.search_by_item(item)
                        poi = {"name": item.text(), "from": value["from"], "type": item.toolTip(), "rtnPara": [],
                               "rtnFnc": ""}
                        pois_checked.append(poi)

            sort = sorted(pois_checked, key=lambda i: i["from"])

            global thread
            self.main.setWindowTitle("BEAT | Running " + Singleton.get_project())
            thread = model.Analysis.DynamicThread.DynamicThread(rlocal=r2, pois=sort)
            thread.textSignal.connect(lambda x: self.terminal(x))
            thread.stopSignal.connect(self.set_stop_title)
            thread.listSignal.connect(lambda x: self.return_funcitions(x))
            thread.start()

    def return_funcitions(self, text):

        value = DBConnection.search_by_name(text["name"], "Functions")
        project_db = DBConnection.get_collection(Singleton.get_project())
        db_info = project_db["functions"]
        if value is not None:
            id = value["_id"]

            index = {"_id": id}
            runs = value["runs"]
            run = {"rtnPara": text["rtnPara"], "rtnFnc": text["rtnFnc"]}
            runs.append(run)
            new_value = {"$set": {"runs": runs}}
            db_info.update_one(index, new_value)

    def stop(self):
        try:
            thread.terminate()
            self.set_stop_title()
        except:
            x = ErrorDialog(self.analysis_tab, "Run a dynamic analysis first", "Dynamic Analysis Error")
            x.exec_()

    def set_stop_title(self):
        self.main.setWindowTitle("BEAT | " + Singleton.get_project())
