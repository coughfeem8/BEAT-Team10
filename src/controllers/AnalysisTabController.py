from PyQt5 import QtCore, QtWidgets, QtGui
from model import Analysis, DBConnection, Plugin
from model.Singleton import Singleton
from view.pop import ErrorDialog
import subprocess


class AnalysisTabController:

    def __init__(self, analysisTab, mainA):
        super().__init__()
        self.analysisTab = analysisTab
        self.main = mainA

    def establish_connections(self):
        self.analysisTab.static_run_button.clicked.connect(self.static)
        self.analysisTab.poi_comboBox.currentIndexChanged.connect(
            lambda x: self.poi_comboBox_change(text=self.analysisTab.poi_comboBox.currentText()))
        self.analysisTab.poi_listWidget.itemClicked.connect(
            lambda x: self.detailed_poi(self.analysisTab.poi_listWidget.currentItem()))
        self.analysisTab.dynamic_run_button.clicked.connect(self.dynamic)
        self.analysisTab.comment_PushButton.clicked.connect(self.comment)
        self.analysisTab.dynamic_stop_button.clicked.connect(self.stop)
        self.analysisTab.output_PushButton.clicked.connect(self.output)

    def establish_calls(self):
        self.setPlugins()
        self.analysisTab.terminal_output_textEdit.setReadOnly(True)

    def setPlugins(self):
        self.analysisTab.plugin_comboBox.clear()
        for pl in Plugin.get_installed_plugins():
            self.analysisTab.plugin_comboBox.addItem(pl)

    def static(self):
        s = Singleton.get_project()
        if (s == "BEAT"):
            x = ErrorDialog(self.analysisTab,"Please select a project","Static Analysis Error")
            x.exec_()
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.analysisTab.poi_listWidget.clear()
        rlocal = Analysis.staticAll(Singleton.get_path())
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
            x = ErrorDialog(self.analysisTab,str(e), "Static Analysis Error")
            x.exec_()
        rlocal.quit()
        QtWidgets.QApplication.restoreOverrideCursor()

    def dynamic(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self.analysisTab, "Dynamic Analysis", "Args to pass:",
                                                         QtWidgets.QLineEdit.Normal, "")

        if okPressed:
            poisChecked = []
            r2 = Analysis.staticAll(Singleton.get_path())
            self.terminal(r2.cmd("doo %s" %text))

            for i in range(self.analysisTab.poi_listWidget.count()):
                item = self.analysisTab.poi_listWidget.item(i)
                if item.checkState() == QtCore.Qt.Checked:
                    poisChecked.append(item)
            for ix in poisChecked:
                value = DBConnection.search_by_item(ix)
                oc = value["from"]
                r2breakpoint = 'db ' + oc

                self.terminal(r2.cmd(r2breakpoint))

            global thread
            self.main.setWindowTitle("BEAT | Running " + Singleton.get_project())
            thread = Analysis.DynamicThread(rlocal=r2)
            thread.text_signal.connect(lambda x:self.terminal(x))
            thread.stop_signal.connect(self.setStopTitle)
            thread.start()

    def stop(self):
        try:
            thread.terminate()
            self.setStopTitle()
        except:
            x = ErrorDialog(self.analysisTab,"Run a dynamic analysis first", "Dynamic Analysis Error")
            x.exec_()

    def poi_comboBox_change(self, text):
        s = Singleton.get_project()
        if s == "BEAT":
            msg = ErrorDialog(self.analysisTab,"Please select a project first", "Static Analysis Error")
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

    def detailed_poi(self, item):
        value = DBConnection.search_by_item(item)
        if value is not None:
            del value["_id"]
            y = str(value)
            self.analysisTab.poi_content_area_textEdit.setPlainText(y)

    def comment(self):
        def open_comment(self):
            s = Singleton.get_project()
            item = self.analysisTab.poi_listWidget.currentItem()
            value = DBConnection.search_by_item(item)
            projectDb = DBConnection.get_collection(s)
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

    def set_item(self, text, type):
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(type)
        return item

    def terminal(self, text):
        if text is not "":
            lastText = self.analysisTab.terminal_output_textEdit.toPlainText()
            self.analysisTab.terminal_output_textEdit.setText(lastText + text + "\n")
            self.analysisTab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)

    def setStopTitle(self):
        self.main.setWindowTitle("BEAT | "+Singleton.get_project())

    def output(self):
        poisChecked = []
        for i in range(self.analysisTab.poi_listWidget.count()):
            item = self.analysisTab.poi_listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                value = DBConnection.search_by_item(item)
                #print(value)
                if item.toolTip() == "Functions":
                    output = Plugin.get_output(value["name"],self.analysisTab.plugin_comboBox.currentText())
                    tmp = {"name":value["name"],"from":value["from"], "output":output }
                elif item.toolTip() == "Strings":
                    output = value['string']
                    tmp = {"name":value['string'], "from": value["from"], "output":output}

                poisChecked.append(tmp)


        try:

            poisChecked.insert(0,"./plugins/output.py")
            pipe = subprocess.Popen(["python", poisChecked[0]],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            pipe.stdin.write("Hello")
            print(pipe.communicate()[0])
            pipe.stdin.close()

        except FileNotFoundError:
            print("not found")
        except Exception as e:

            ErrorDialog(self.analysisTab,str(e), "Error")