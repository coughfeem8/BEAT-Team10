from PyQt5 import QtCore, QtGui, QtWidgets
import r2pipe
from os import walk
from model.singleton import Singleton
from model import dbconnection


class project_tab_controller:

    def __init__(self, projectTab, mainA):
        global mainWin
        mainWin = mainA
        global activeProject
        global saved
        saved = False
        self.nameProject = ""
        self.projectTab = projectTab

    def establish_connections(self):
        self.projectTab.listWidget.itemSelectionChanged.connect(self.itemActivated_event)
        self.projectTab.pushButton_7.clicked.connect(self.createProject)
        self.projectTab.pushButton_8.clicked.connect(self.BrowseBnryFiles)
        self.projectTab.pushButton_9.clicked.connect(self.deleteProject)
        self.projectTab.pushButton_10.clicked.connect(self.SaveProject)
        self.projectTab.lineEdit.textChanged.connect(
            lambda x: self.search_saved_projects(self.projectTab.lineEdit.text()))

    def establish_calls(self):
        self.projectTab.pushButton_10.setEnabled(False)
        self.projectTab.pushButton_8.setEnabled(False)
        self.projectTab.lineEdit_2.setReadOnly(True)
        self.projectTab.textEdit_2.setReadOnly(True)
        self.searchProjects()
        self.fillBnryPropEmpty()
        self.setPlugins()

    def setPlugins(self):
        f = []
        for (dirpath, dirnames, filenames) in walk('./plugins'):
            for name in filenames:
                if name.endswith('.xml'):
                    f.append(name)
            break
        Singleton.setPlugins(f)

    def fillBnryPropEmpty(self):
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

    def fillBnryProp(self, r2BinInfo):
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["os"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["arch"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["core"]["type"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["machine"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["class"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["bits"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["lang"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["canary"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["crypto"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["nx"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["pic"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["endian"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.projectTab.tableWidget.setItem(11, 1, item)

    def BrowseBnryFiles(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.projectTab, "Browse Binary File", "",
                                                            "Binary Files (*.exe | *.elf | *.out)", options=options)

        if fileName:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            try:
                global r2BinInfo
                self.projectTab.lineEdit_3.setText(fileName)
                rlocal = r2pipe.open(fileName)
                r2BinInfo = rlocal.cmdj("ij")

                if r2BinInfo["core"]["format"] == "any":
                    msg = QtWidgets.QMessageBox()
                    msg.setText("Error")
                    return

                self.fillBnryProp(r2BinInfo)

            except Exception as e:
                msg = QtWidgets.QMessageBox()
                msg.setText(str(e))
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = msg.exec_()
            QtWidgets.QApplication.restoreOverrideCursor()

    def SaveProject(self):
        if self.projectTab.lineEdit_3.text() != "":
            saved = False
            projectDb = dbconnection.getCollection(self.nameProject)
            projInfo = projectDb["projectInfo"]
            info = {"ProjectName": self.projectTab.lineEdit_2.text(),
                    "ProjectDescription": self.projectTab.textEdit_2.toPlainText(),
                    "BnyFilePath": self.projectTab.lineEdit_3.text()}
            insertInfo = projInfo.insert(info, check_keys=False)
            binInfo = projectDb["binaryInfo"]
            insertObj = binInfo.insert(r2BinInfo, check_keys=False)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Save Project")
            msg.setText("Project Saved")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            self.projectTab.pushButton_8.setEnabled(False)
            self.projectTab.pushButton_10.setEnabled(False)
            for item_at in range(self.projectTab.listWidget.count()):
                self.projectTab.listWidget.item(item_at).setFlags(self.projectTab.listWidget.item(item_at).flags() | QtCore.Qt.ItemIsSelectable)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please select a Binary File")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()

    def createProject(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self.projectTab, "Create New Project", "Name of Project:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            dbnames = dbconnection.getDB()
            if text in dbnames:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Project with that name already exists")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = msg.exec_()
                return
            self.projectTab.lineEdit_2.setText(text)
            self.projectTab.textEdit_2.setText("")
            self.projectTab.lineEdit_3.setText("")
            self.fillBnryPropEmpty()
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
                self.projectTab.listWidget.item(item_at).setFlags(self.projectTab.listWidget.item(item_at).flags() & ~QtCore.Qt.ItemIsSelectable)

    def itemActivated_event(self):
        if self.projectTab.listWidget.count() != 0:
            project = self.projectTab.listWidget.selectedItems()
            projectName = [item.text().encode("ascii") for item in project]
            if projectName:
                self.nameProject = str(projectName[0], 'utf-8')
                try:
                    Singleton.setProject(self.nameProject)
                    projectDb = dbconnection.getCollection(self.nameProject)
                    projInfo = projectDb["projectInfo"]
                    binInfo = projectDb["binaryInfo"]
                    cursor = projInfo.find()
                    for db in cursor:
                        self.projectTab.textEdit_2.setPlainText(db['ProjectDescription'])
                        self.projectTab.lineEdit_2.setText(db['ProjectName'])
                        self.projectTab.lineEdit_3.setText(db['BnyFilePath'])
                        Singleton.setPath(db['BnyFilePath'])
                    cursorBin = binInfo.find()
                    for db in cursorBin:
                        self.fillBnryPropEmpty()
                        self.fillBnryProp(db)
                    if (saved):
                        mainWin.setWindowTitle("* " + self.nameProject)
                    else:
                        mainWin.setWindowTitle("BEAT | " + self.nameProject)

                except Exception as e:
                    msg = QtWidgets.QMessageBox()
                    msg.setText(str(e))
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    retval = msg.exec_()

    def searchProjects(self):
        cursor = dbconnection.getDB()
        self.projectTab.listWidget.clear()
        for db in cursor:
            if db not in ['admin', 'local', 'config']:
                self.projectTab.listWidget.addItem(db)

    def deleteProject(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        if self.nameProject != "":
            buttonReply = QtWidgets.QMessageBox.question(self.projectTab, 'PyQt5 message',
                                                         "Do you like to erase Project %s ?" % self.nameProject,
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                         QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:

                dbconnection.dropDB(self.nameProject)

                self.projectTab.lineEdit_2.setText("")
                self.projectTab.textEdit_2.setText("")
                self.projectTab.lineEdit_3.setText("")
                self.fillBnryPropEmpty()
                self.projectTab.pushButton_8.setEnabled(False)
                self.projectTab.pushButton_10.setEnabled(False)
                for item_at in range(self.projectTab.listWidget.count()):
                    self.projectTab.listWidget.item(item_at).setFlags(self.projectTab.listWidget.item(item_at).flags() | QtCore.Qt.ItemIsSelectable)
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