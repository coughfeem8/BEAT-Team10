from PyQt5 import QtCore, QtGui, QtWidgets
import r2pipe
from os import walk
from model.Singleton import Singleton
from model import DBConnection


class ProjectTabController:

    def __init__(self, project_tab, main):
        global main_win
        main_win = main
        global active_project
        global saved
        saved = False
        self.nameProject = ""
        self.projectTab = project_tab

    def establish_connections(self):
        self.projectTab.listWidget.itemSelectionChanged.connect(self.item_activated_event)
        self.projectTab.pushButton_7.clicked.connect(self.create_project)
        self.projectTab.pushButton_8.clicked.connect(self.browse_binary_files)
        self.projectTab.pushButton_9.clicked.connect(self.delete_project)
        self.projectTab.pushButton_10.clicked.connect(self.save_project)
        self.projectTab.lineEdit.textChanged.connect(
            lambda x: self.search_saved_projects(self.projectTab.lineEdit.text()))

    def establish_calls(self):
        self.projectTab.pushButton_10.setEnabled(False)
        self.projectTab.pushButton_8.setEnabled(False)
        self.projectTab.lineEdit_2.setReadOnly(True)
        self.projectTab.textEdit_2.setReadOnly(True)
        self.search_projects()
        self.fill_binary_prop_empty()
        self.set_plugins()

    def set_plugins(self):
        f = []
        for (dir_path, dir_names, filenames) in walk('./plugins'):
            for name in filenames:
                if name.endswith('.xml'):
                    f.append(name)
            break
        Singleton.set_plugins(f)

    def fill_binary_prop_empty(self):
        properties = ["OS", "Arch", "Binary Type", "Machine", "Class", "Bits", "Language", "Canary", "Cripto", "Nx",
                      "Pic", "Endian"]

        self.projectTab.tableWidget.setObjectName("tableWidget")
        self.projectTab.tableWidget.setColumnCount(2)
        self.projectTab.tableWidget.setRowCount(12)
        self.projectTab.tableWidget.horizontalHeader().hide()
        self.projectTab.tableWidget.verticalHeader().hide()
        self.projectTab.tableWidget.horizontalHeader().setStretchLastSection(True)

        bolds = QtGui.QFont()
        QtGui.QFont.setBold(bolds, True)
        for x in range(len(properties)):
            item = QtWidgets.QTableWidgetItem(properties[x])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            empty = QtWidgets.QTableWidgetItem("")
            empty.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setFont(bolds)
            self.projectTab.tableWidget.setItem(x, 0, item)
            self.projectTab.tableWidget.setItem(x, 1, empty)

    def fill_binary_prop(self, r2_bin_info):
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["os"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["arch"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["core"]["type"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["machine"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["class"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["bits"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["lang"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["canary"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["crypto"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["nx"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["pic"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["endian"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(11, 1, item)

    def browse_binary_files(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.projectTab, "Browse Binary File", "",
                                                             "Binary Files (*.exe | *.elf | *.out)", options=options)

        if file_name:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            try:
                global r2_bin_info
                self.projectTab.lineEdit_3.setText(file_name)
                rlocal = r2pipe.open(file_name)
                r2_bin_info = rlocal.cmdj("ij")

                if r2_bin_info["core"]["format"] == "any":
                    msg = QtWidgets.QMessageBox()
                    msg.setText("Error")
                    return

                self.fill_binary_prop(r2_bin_info)

            except Exception as e:
                msg = QtWidgets.QMessageBox()
                msg.setText(str(e))
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = msg.exec_()
            QtWidgets.QApplication.restoreOverrideCursor()

    def save_project(self):
        if self.projectTab.lineEdit_3.text() != "":
            saved = False
            projectDb = DBConnection.get_collection(self.nameProject)
            projInfo = projectDb["projectInfo"]
            info = {"ProjectName": self.projectTab.lineEdit_2.text(),
                    "ProjectDescription": self.projectTab.textEdit_2.toPlainText(),
                    "BnyFilePath": self.projectTab.lineEdit_3.text()}
            insert_info = projInfo.insert(info, check_keys=False)
            bin_info = projectDb["binaryInfo"]
            insert_obj = bin_info.insert(r2_bin_info, check_keys=False)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Save Project")
            msg.setText("Project Saved")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            self.projectTab.pushButton_8.setEnabled(False)
            self.projectTab.pushButton_10.setEnabled(False)
            for item_at in range(self.projectTab.listWidget.count()):
                self.projectTab.listWidget.item(item_at).setFlags(
                    self.projectTab.listWidget.item(item_at).flags() | QtCore.Qt.ItemIsSelectable)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please select a Binary File")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()

    def create_project(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self.projectTab, "Create New Project", "Name of Project:",
                                                          QtWidgets.QLineEdit.Normal, "")
        if ok_pressed and text != '':
            db_names = DBConnection.get_db()
            if text in db_names:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Project with that name already exists")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = msg.exec_()
                return
            self.projectTab.lineEdit_2.setText(text)
            self.projectTab.textEdit_2.setText("")
            self.projectTab.lineEdit_3.setText("")
            self.fill_binary_prop_empty()
            self.nameProject = text
            self.projectTab.listWidget.addItem(text)
            item = self.projectTab.listWidget.findItems(text, QtCore.Qt.MatchExactly)
            self.projectTab.listWidget.setCurrentItem(item[0])
            self.projectTab.setWindowTitle('Create Project')
            saved = True
            self.projectTab.pushButton_8.setEnabled(True)
            self.projectTab.pushButton_10.setEnabled(True)
            self.projectTab.textEdit_2.setReadOnly(False)
            for item_at in range(self.projectTab.listWidget.count()):
                self.projectTab.listWidget.item(item_at).setFlags(
                    self.projectTab.listWidget.item(item_at).flags() & ~QtCore.Qt.ItemIsSelectable)

    def item_activated_event(self):
        if self.projectTab.listWidget.count() != 0:
            project = self.projectTab.listWidget.selectedItems()
            project_name = [item.text().encode("ascii") for item in project]
            if project_name:
                self.nameProject = str(project_name[0], 'utf-8')
                try:
                    Singleton.set_project(self.nameProject)
                    project_db = DBConnection.get_collection(self.nameProject)
                    project_info = project_db["projectInfo"]
                    bin_info = project_db["binaryInfo"]
                    cursor = project_info.find()
                    for db in cursor:
                        self.projectTab.textEdit_2.setPlainText(db['ProjectDescription'])
                        self.projectTab.lineEdit_2.setText(db['ProjectName'])
                        self.projectTab.lineEdit_3.setText(db['BnyFilePath'])
                        Singleton.set_path(db['BnyFilePath'])
                    cursor_bin = bin_info.find()
                    for db in cursor_bin:
                        self.fill_binary_prop_empty()
                        self.fill_binary_prop(db)
                    if saved:
                        main_win.setWindowTitle("* " + self.nameProject)
                    else:
                        main_win.setWindowTitle("BEAT | " + self.nameProject)

                except Exception as e:
                    msg = QtWidgets.QMessageBox()
                    msg.setText(str(e))
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    retval = msg.exec_()

    def search_projects(self):
        cursor = DBConnection.get_db()
        self.projectTab.listWidget.clear()
        for db in cursor:
            if db not in ['admin', 'local', 'config']:
                self.projectTab.listWidget.addItem(db)

    def delete_project(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        if self.nameProject != "":
            button_reply = QtWidgets.QMessageBox.question(self.projectTab, 'PyQt5 message',
                                                          "Do you like to erase Project %s ?" % self.nameProject,
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
            if button_reply == QtWidgets.QMessageBox.Yes:

                DBConnection.drop_db(self.nameProject)

                self.projectTab.lineEdit_2.setText("")
                self.projectTab.textEdit_2.setText("")
                self.projectTab.lineEdit_3.setText("")
                self.fill_binary_prop_empty()
                self.projectTab.pushButton_8.setEnabled(False)
                self.projectTab.pushButton_10.setEnabled(False)
                for item_at in range(self.projectTab.listWidget.count()):
                    self.projectTab.listWidget.item(item_at).setFlags(
                        self.projectTab.listWidget.item(item_at).flags() | QtCore.Qt.ItemIsSelectable)
                listItems = self.projectTab.listWidget.selectedItems()
                if not listItems:
                    return
                for item in listItems:
                    self.projectTab.listWidget.takeItem(self.projectTab.listWidget.row(item))
        else:
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()

    def search_saved_projects(self, text):
        if len(text) is not 0:
            search_result = self.projectTab.listWidget.findItems(text, QtCore.Qt.MatchContains)
            for item in range(self.projectTab.listWidget.count()):
                self.projectTab.listWidget.item(item).setHidden(True)
            for item in search_result:
                item.setHidden(False)
        else:
            for item in range(self.projectTab.listWidget.count()):
                self.projectTab.listWidget.item(item).setHidden(False)
