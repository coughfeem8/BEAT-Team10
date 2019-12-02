from PyQt5 import QtCore, QtGui, QtWidgets
from model.Singleton import Singleton
from model import DBConnection, r2Connection
from view.pop.ErrorDialog import ErrorDialog
from controllers.Controller import Controller


class ProjectTabController(Controller):
    project_creation_started = QtCore.pyqtSignal()
    project_creation_finished = QtCore.pyqtSignal()
    selected_project_changed = QtCore.pyqtSignal()

    def __init__(self, project_tab):
        super().__init__()
        self.project_tab = project_tab
        self.project_name = ""

    def establish_connections(self):
        self.project_tab.listWidget.itemSelectionChanged.connect(self.project_selected_changed)
        self.project_tab.pushButton_7.clicked.connect(self.create_project)
        self.project_tab.pushButton_8.clicked.connect(self.browse_binary_files)
        self.project_tab.pushButton_9.clicked.connect(self.delete_project)
        self.project_tab.pushButton_10.clicked.connect(self.save_project)
        self.project_tab.lineEdit.textChanged.connect(
            lambda: self.search_list(self.project_tab.listWidget, self.project_tab.lineEdit.text()))

    def establish_calls(self):
        self.project_tab.pushButton_10.setEnabled(False)
        self.project_tab.pushButton_8.setEnabled(False)
        self.project_tab.lineEdit_2.setReadOnly(True)
        self.project_tab.textEdit_2.setReadOnly(True)
        self.search_projects()
        self.set_binary_prop()

    def set_binary_prop(self):
        properties = ["OS", "Arch", "Binary Type", "Machine", "Class", "Bits", "Language", "Canary", "Cripto", "Nx",
                      "Pic", "Endian"]

        self.project_tab.tableWidget.setObjectName("tableWidget")
        self.project_tab.tableWidget.setColumnCount(2)
        self.project_tab.tableWidget.setRowCount(12)
        self.project_tab.tableWidget.horizontalHeader().hide()
        self.project_tab.tableWidget.verticalHeader().hide()
        self.project_tab.tableWidget.horizontalHeader().setStretchLastSection(True)

        bolds = QtGui.QFont()
        QtGui.QFont.setBold(bolds, True)
        for x in range(len(properties)):
            item = QtWidgets.QTableWidgetItem(properties[x])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            empty = QtWidgets.QTableWidgetItem("")
            empty.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setFont(bolds)
            self.project_tab.tableWidget.setItem(x, 0, item)
            self.project_tab.tableWidget.setItem(x, 1, empty)

    def fill_binary_prop(self, r2_bin_info):
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["os"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["arch"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["core"]["type"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["machine"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["class"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["bits"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["lang"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["canary"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["crypto"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["nx"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2_bin_info["bin"]["pic"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem(r2_bin_info["bin"]["endian"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.project_tab.tableWidget.setItem(11, 1, item)

    def browse_binary_files(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.project_tab, "Browse Binary File", "",
                                                             "Binary Files (*.exe | *.elf | *.out)", options=options)

        if file_name:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            try:
                global r2_bin_info
                self.project_tab.lineEdit_3.setText(file_name)
                rlocal = r2Connection.Open(file_name)
                r2_bin_info = rlocal.cmdj("ij")

                if r2_bin_info["core"]["format"] == "any":
                    msg = QtWidgets.QMessageBox()
                    msg.setText("Error")
                    return

                self.fill_binary_prop(r2_bin_info)

            except Exception as e:
                x = ErrorDialog(self.project_tab, str(e), "Error")
                x.exec_()
            QtWidgets.QApplication.restoreOverrideCursor()

    def create_project(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self.project_tab, "Create New Project", "Name of Project:",
                                                          QtWidgets.QLineEdit.Normal, "")
        if ok_pressed and text != '':
            db_names = DBConnection.get_db()
            if text in db_names:
                msg = ErrorDialog(self.project_tab,"Project with that name already exists", "Error Creating Project")
                msg.exec_()
                return
            self.project_tab.lineEdit_2.setText(text)
            self.project_tab.textEdit_2.setText("")
            self.project_tab.lineEdit_3.setText("")
            self.project_tab.textEdit_2.setReadOnly(False)
            self.set_binary_prop()
            self.project_name = text
            self.project_tab.listWidget.addItem(text)
            item = self.project_tab.listWidget.findItems(text, QtCore.Qt.MatchExactly)
            self.project_tab.listWidget.setCurrentItem(item[0])
            self.project_tab.setWindowTitle('Create Project')
            saved = True
            self.create_operations(self.project_creation_started, [self.project_tab.pushButton_7],
                                        [self.project_tab.pushButton_8, self.project_tab.pushButton_10],
                                        self.project_tab.listWidget)

    def save_project(self):
        if self.project_tab.lineEdit_3.text() != "":
            saved = False
            project_db = DBConnection.get_collection(self.project_name)
            project_info = project_db["projectInfo"]
            info = {"ProjectName": self.project_tab.lineEdit_2.text(),
                    "ProjectDescription": self.project_tab.textEdit_2.toPlainText(),
                    "BnyFilePath": self.project_tab.lineEdit_3.text()}
            insert_info = project_info.insert(info, check_keys=False)
            bin_info = project_db["binaryInfo"]
            insert_obj = bin_info.insert(r2_bin_info, check_keys=False)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Save Project")
            msg.setText("Project Saved")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            self.project_tab.textEdit_2.setReadOnly(True)
            self.delete_save_operations(self.project_creation_finished, [self.project_tab.pushButton_7],
                                   [self.project_tab.pushButton_8, self.project_tab.pushButton_10],
                                   self.project_tab.listWidget)

        else:
            msg = ErrorDialog(self.project_tab, "Please select a binary file", "Error Saving Project")
            msg.exec_()

    def delete_project(self):
        if self.project_name != "":
            button_reply = QtWidgets.QMessageBox.question(self.project_tab, 'PyQt5 message',
                                                          "Do you like to erase Project %s ?" % self.project_name,
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
            if button_reply == QtWidgets.QMessageBox.Yes:

                DBConnection.drop_db(self.project_name)

                self.project_tab.lineEdit_2.setText("")
                self.project_tab.textEdit_2.setText("")
                self.project_tab.lineEdit_3.setText("")
                self.set_binary_prop()
                self.delete_save_operations(self.project_creation_finished, [self.project_tab.pushButton_7],
                                            [self.project_tab.pushButton_8, self.project_tab.pushButton_10],
                                            self.project_tab.listWidget)

                list_items = self.project_tab.listWidget.selectedItems()
                if not list_items:
                    return
                for item in list_items:
                    self.project_tab.listWidget.takeItem(self.project_tab.listWidget.row(item))
        else:
            msg = ErrorDialog(self.project_tab, "Please select a project", "Error Deleting Project")
            msg.exec_()

    def project_selected_changed(self):
        if self.project_tab.listWidget.count() != 0:
            project = self.project_tab.listWidget.selectedItems()
            project_name = [item.text().encode("ascii") for item in project]
            if project_name:
                self.project_name = str(project_name[0], 'utf-8')
                try:
                    Singleton.set_project(self.project_name)
                    project_db = DBConnection.get_collection(self.project_name)
                    project_info = project_db["projectInfo"]
                    bin_info = project_db["binaryInfo"]
                    cursor = project_info.find()
                    for db in cursor:
                        self.project_tab.textEdit_2.setPlainText(db['ProjectDescription'])
                        self.project_tab.lineEdit_2.setText(db['ProjectName'])
                        self.project_tab.lineEdit_3.setText(db['BnyFilePath'])
                        Singleton.set_path(db['BnyFilePath'])
                    cursor_bin = bin_info.find()
                    for db in cursor_bin:
                        self.set_binary_prop()
                        self.fill_binary_prop(db)
                    self.selected_project_changed.emit()
                except Exception as e:
                    msg = ErrorDialog(self.project_tab, str(e), "Error")
                    msg.exec()

    def search_projects(self):
        cursor = DBConnection.get_db()
        self.project_tab.listWidget.clear()
        for db in cursor:
            if db not in ['admin', 'local', 'config', 'plugin']:
                self.project_tab.listWidget.addItem(db)
