from PyQt5 import QtCore, QtWidgets, QtGui
import subprocess
import model.Analysis.DynamicThread
import model.Analysis.StaticAnalysis
from model import DBConnection, Plugin
from model.Singleton import Singleton
from view.pop.ErrorDialog import ErrorDialog
from view.pop.CommentDialog import CommentDialog
from controllers.POIFormatter import format_poi
from controllers.Controller import Controller


class AnalysisTabController(Controller):
    dynamic_started = QtCore.pyqtSignal()
    dynamic_stopped = QtCore.pyqtSignal()

    def __init__(self, analysis_tab):
        super().__init__()
        self.analysis_tab = analysis_tab
        self.analysis_tab.poi_content_area_textEdit.setStyleSheet('')
        self.run = 0


    def establish_connections(self):
        self.analysis_tab.static_run_button.clicked.connect(self.static)
        self.analysis_tab.poi_comboBox.currentIndexChanged.connect(
            lambda: self.poi_comboBox_change(text=self.analysis_tab.poi_comboBox.currentText()))
        self.analysis_tab.poi_listWidget.itemClicked.connect(
            lambda: self.detailed_poi(self.analysis_tab.poi_listWidget.currentItem()))
        self.analysis_tab.dynamic_run_button.clicked.connect(self.dynamic)
        self.analysis_tab.comment_PushButton.clicked.connect(self.open_comment)
        self.analysis_tab.output_PushButton.clicked.connect(self.open_output)
        self.analysis_tab.dynamic_stop_button.clicked.connect(self.stop)
        self.analysis_tab.search_bar_lineEdit.textChanged.connect(
            lambda: self.search_list(self.analysis_tab.poi_listWidget, self.analysis_tab.search_bar_lineEdit.text()))
        self.analysis_tab.terminal_window_lineEdit.returnPressed.connect(
            lambda: self.input_terminal(self.analysis_tab.terminal_window_lineEdit.text()))
        self.analysis_tab.poi_listWidget.itemDoubleClicked.connect(
            lambda: self.detailed_poi(self.analysis_tab.poi_listWidget.currentItem()))

    def establish_calls(self):
        self.analysis_tab.terminal_output_textEdit.setReadOnly(True)
        self.set_plugins()


    def set_plugins(self):
        """
        This method check which plugins are on the database and add them to the drop down list for changing the plugin.
        :return: none
        """
        self.analysis_tab.plugin_comboBox.clear()
        for pl in Plugin.get_installed_plugins():
            self.analysis_tab.plugin_comboBox.addItem(pl)


    def set_item(self, text, poi_type):
        """
        Crewates a list widget item with the given text.
        :param text: name of item(poi's name)
        :param poi_type: poi's type
        :return: list widget item
        """
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(poi_type)
        return item


    def static(self):
        """
        This method listens to the click of the static analysis button and connects with the model to preform
        static analysis.This method also saves into the database depending on the type.
        :return: none
        """
        s = Singleton.get_project()
        if s == "BEAT":
            x = ErrorDialog(self.analysis_tab, "Please select a project", "Static Analysis Error")
            x.exec_()
            return
        if self.analysis_tab.plugin_comboBox.count() == 0:
            x = ErrorDialog(self.analysis_tab, "Please install a plugin", "Static Analysis Error")
            x.exec_()
            return

        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.analysis_tab.poi_listWidget.clear()
        rlocal = model.Analysis.StaticAnalysis.static_all(Singleton.get_path())
        try:
            if self.analysis_tab.poi_comboBox.currentText() == "All":

                strings = model.Analysis.StaticAnalysis.static_strings(rlocal,
                                                                       self.analysis_tab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    item = self.change_font(item)
                    self.analysis_tab.poi_listWidget.addItem(item)

                functions = model.Analysis.StaticAnalysis.static_functions(rlocal,
                                                                           self.analysis_tab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    item = self.change_font(item)
                    self.analysis_tab.poi_listWidget.addItem(item)

            elif self.analysis_tab.poi_comboBox.currentText() == "Functions":

                functions = model.Analysis.StaticAnalysis.static_functions(rlocal,
                                                                           self.analysis_tab.plugin_comboBox.currentText())
                for fc in functions:
                    item = self.set_item(fc, "Functions")
                    item = self.change_font(item)
                    self.analysis_tab.poi_listWidget.addItem(item)

            elif self.analysis_tab.poi_comboBox.currentText() == "Strings":

                strings = model.Analysis.StaticAnalysis.static_strings(rlocal,
                                                                       self.analysis_tab.plugin_comboBox.currentText())
                for st in strings:
                    item = self.set_item(st, "Strings")
                    item = self.change_font(item)
                    self.analysis_tab.poi_listWidget.addItem(item)

        except Exception as e:
            x = ErrorDialog(self.analysis_tab, str(e), "Static Analysis Error")
            x.exec_()
        rlocal.quit()
        QtWidgets.QApplication.restoreOverrideCursor()



    def poi_comboBox_change(self, text):
        """
        This function listens for a change in the  poi window to change the current filter and updates the
        filtered pois which are stored in the database in the list view
        :param text: poi's type
        :return: none
        """
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
                item = self.change_font(item)
                self.analysis_tab.poi_listWidget.addItem(item)
        elif text == "Strings":
            project_info = project_db["string"]
            cursor = project_info.find()
            for db in cursor:
                text = db["string"]
                item = self.set_item(text, "Strings")
                item = self.change_font(item)
                self.analysis_tab.poi_listWidget.addItem(item)

        elif text == "All":
            project_info = project_db["functions"]
            cursor = project_info.find()
            for db in cursor:
                item = self.set_item(db["name"], "Functions")
                item = self.change_font(item)
                self.analysis_tab.poi_listWidget.addItem(item)
            project_info = project_db["string"]
            cursor = project_info.find()
            for db in cursor:
                text = db["string"]
                item = self.set_item(text, "Strings")
                item = self.change_font(item)
                self.analysis_tab.poi_listWidget.addItem(item)


    def detailed_poi(self, item):
        """
        This method gets the information of an existing poi in the database and displays it top the detail point of
        interest edit box.
         :param item: current selected poi
         :return: none
        """
        value = DBConnection.search_by_item(item)
        if value is not None:
            del value["_id"]
            y = value
            self.analysis_tab.poi_content_area_textEdit.setText(format_poi(y))

    def open_comment(self):
        """
        This method opens the comment pop-up to add a comment/ or edit an exiting comment.Afterwards it updates
        the information to the detailed point of interest in the database.
        :return: none
        """
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
        """
        Grabs the output file from the plugin and gets the selcted pois and runs the file with the pois as arguments.
        :return: none
        """
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
            subprocess.check_call(cmd)
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
        """
        Display information in the terminal text edit widget.
        :param text: text to display
        :return: none
        """
        if text is not "":
            last_text = self.analysis_tab.terminal_output_textEdit.toPlainText()
            self.analysis_tab.terminal_output_textEdit.setText(last_text + text + "\n")
            self.analysis_tab.terminal_output_textEdit.moveCursor(QtGui.QTextCursor.End)

    def dynamic(self):
        """
        This method asks the user for parameters, creates a list with the selected pois and  stats dynamic analysis
        thread with the list of pois and parameters as arguments.
         :return:
        """
        if self.analysis_tab.poi_listWidget.count() == 0:
            x = ErrorDialog(self.analysis_tab, "Please run Static Analysis first", "Error in DYnamic Analysis")
            x.exec_()
            return
        global input
        input, ok_pressed = QtWidgets.QInputDialog.getText(self.analysis_tab, "Dynamic Analysis", "Args to pass:",
                                                          QtWidgets.QLineEdit.Normal, "")

        if ok_pressed:
            self.run += 1
            pois_checked = []

            r2 = model.Analysis.StaticAnalysis.static_all(Singleton.get_path())
            self.terminal('r2 > \n')
            self.terminal(r2.cmd("doo %s" % input))

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
            try:
                self.run = 1
                self.dynamic_started.emit()
                thread = model.Analysis.DynamicThread.DynamicThread(rlocal=r2, pois=sort)
                thread.textSignal.connect(lambda x: self.terminal(x))
                thread.listSignal.connect(lambda x: self.return_funcitions(x))
                thread.errorSignal.connect(lambda x: self.error_thread(x))
                thread.start()
            except Exception as e:
                print(e)

    def error_thread(self, text):
        msg = ErrorDialog(self.analysis_tab,text,"Error in Dynamic Analysis")
        msg.exec_()



    def return_funcitions(self, text):
        """ This method receives the information from the breakpoint and stores the information into the database.
        :param text: information received
        :return: none
        """
        value = DBConnection.search_by_name(text["name"], "Functions")
        project_db = DBConnection.get_collection(Singleton.get_project())
        db_info = project_db["functions"]
        if value is not None:
            id = value["_id"]

            index = {"_id": id}
            runs = value["runs"]
            run = {"name":input,"rtnPara": text["rtnPara"], "rtnFnc": text["rtnFnc"]}
            runs.append(run)
            new_value = {"$set": {"runs": runs}}
            db_info.update_one(index, new_value)

    def stop(self):
        """
         This method kills the running dynamic thread.
        :return: none
        """
        try:
            thread.terminate()
            self.run = 0
            self.dynamic_stopped.emit()
        except:
            x = ErrorDialog(self.analysis_tab, "Run a dynamic analysis first", "Dynamic Analysis Error")
            x.exec_()

    def input_terminal(self, text):
        """
        This method checks if the dynamic analysis thread is running if it's being run it passes the text as an input
        pipe.Otherwise passes the text as a command for Radare.
        :param text: text for argument
        :return: none
        """
        if self.run == 0:
            if Singleton.get_project() != "BEAT":
                try:
                    r2 = model.Analysis.StaticAnalysis.static_all(Singleton.get_path())
                    self.terminal(text + ' >\n')
                    self.terminal(r2.cmd(text))
                except Exception as e:
                    x = ErrorDialog(self.analysis_tab, str(e), "Error")
                    x.exec_()
                self.analysis_tab.terminal_window_lineEdit.setText("")
            else:
                x = ErrorDialog(self.analysis_tab, "First select a project", "Error")
                x.exec_()
        elif self.run == 1:
            thread.input(text)
        self.analysis_tab.terminal_window_lineEdit.clear()

    def change_font(self, item):
        """
        This method checks if any poi has a comment then bolds the name of the poi.
        :param item: item list widget to bold the name
        :return: item list widget
        """
        new_font = QtGui.QFont()
        if DBConnection.search_comment_by_item(item):
            new_font.setBold(True)
        else:
            new_font.setBold(False)
        item.setFont(new_font)
        return item
