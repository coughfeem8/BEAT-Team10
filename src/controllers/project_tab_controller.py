from PyQt5 import QtGui, QtCore, QtWidgets
from model import dbconnection, r2connection
from model.singleton import Singleton
from view import pop

class project_tab_controller:

    def __init__(self, projectTab, mainA):
        self.projectTab = projectTab
        self.main = mainA

    def establish_connections(self):
        self.projectTab.listWidget.itemSelectionChanged.connect(self.itemActivated)
        self.projectTab.pushButton_7.clicked.connect(self.createProject)
        self.projectTab.pushButton_8.clicked.connect(self.browseBinary)
        self.projectTab.pushButton_9.clicked.connect(self.deleteProject)
        self.projectTab.pushButton_10.clicked.connect(self.saveProject)

    def establish_calls(self):
        self.fillBnryPropEmpty()
        self.searchProjects()
        self.projectTab.pushButton_10.setEnabled(False)
        self.projectTab.pushButton_8.setEnabled(False)
        self.projectTab.lineEdit_2.setReadOnly(True)
        self.projectTab.textEdit_2.setReadOnly(True)

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

    def searchProjects(self):
        cursor = dbconnection.getDB()
        self.projectTab.listWidget.clear()
        for db in cursor:
            if db not in ['admin', 'local', 'config', 'plugin']:
                self.projectTab.listWidget.addItem(db)

    def createProject(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self.projectTab, "Create New Project", "Name of Project:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            dbnames = dbconnection.getDB()
            if text in dbnames:
                x= pop.errorDialog(self.projectTab,"Project with that name already exists","Error Creating Project")
                x.exec_()
                return
            self.projectTab.lineEdit_2.setText(text)
            self.projectTab.textEdit_2.setText("")
            self.projectTab.lineEdit_3.setText("")
            self.fillBnryPropEmpty()
            Singleton.setProject(text)
            self.projectTab.listWidget.addItem(text)
            item = self.projectTab.listWidget.findItems(text, QtCore.Qt.MatchExactly)
            self.projectTab.listWidget.setCurrentItem(item[0])
            self.main.setWindowTitle("BEAT | *"+text)
            self.projectTab.pushButton_8.setEnabled(True)
            self.projectTab.pushButton_10.setEnabled(True)
            self.projectTab.textEdit_2.setReadOnly(False)

    def saveProject(self):
        if self.projectTab.lineEdit_3.text() != "":
            projectDB = dbconnection.getCollection(Singleton.getProject())
            projInfo = projectDB["projectInfo"]
            info = {"ProjectName": self.projectTab.lineEdit_2.text(),
                    "ProjectDescription": self.projectTab.textEdit_2.toPlainText(),
                    "BnyFilePath": self.projectTab.lineEdit_3.text()}
            projInfo.insert(info, check_keys=False)
            binInfo = projectDB["binaryInfo"]
            binInfo.insert(r2BinInfo, check_keys=False)
            x = pop.errorDialog(self.projectTab,"Project Saved", "Save Project")
            x.exec_()
            self.projectTab.pushButton_8.setEnabled(False)
            self.projectTab.pushButton_10.setEnabled(False)
            self.main.setWindowTitle("BEAT | " + Singleton.getProject())
        else:
            x = pop.errorDialog(self.projectTab,"Please select a binary file", "Error")
            x.exec_()

    def deleteProject(self):
        if Singleton.getProject() != "BEAT":
            buttonReply = QtWidgets.QMessageBox.question(self.projectTab, 'PyQt5 message',
                                                         "Do you like to erase Project %s ?" % Singleton.getProject(),
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                         QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                dbconnection.dropDB(Singleton.getProject())
                Singleton.setProject("BEAT")

                self.projectTab.lineEdit_2.setText("")
                self.projectTab.textEdit_2.setText("")
                self.projectTab.lineEdit_3.setText("")
                self.fillBnryPropEmpty()
                listItems = self.projectTab.listWidget.selectedItems()
                if not listItems: return
                for item in listItems:
                    self.projectTab.listWidget.takeItem(self.projectTab.listWidget.row(item))
        else:
            x = pop.errorDialog(self.projectTab,"Please select a project", "Error")
            x.exec_()

    def browseBinary(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.projectTab, "Browse Binary File", "",
                                                            "Binary Files (*.exe | *.elf | *.out)", options=options)

        if fileName:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            try:
                global r2BinInfo
                self.projectTab.lineEdit_3.setText(fileName)
                rlocal = r2connection.open(fileName)
                r2BinInfo = rlocal.cmdj("ij")

                if (r2BinInfo["core"]["format"] == "any") or (r2BinInfo["bin"]["arch"] != "x86"):
                    x = pop.errorDialog(self.projectTab, "Binary file not supported", "Error")
                    x.exec_()
                    return

                self.fillBnryProp(r2BinInfo)
                rlocal.quit()
            except Exception as e:
                x = pop.errorDialog(self.projectTab,str(e), "Error")
                x.exec_()
            QtWidgets.QApplication.restoreOverrideCursor()

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

    def itemActivated(self):
        if self.projectTab.listWidget.count() != 0:
            project = self.projectTab.listWidget.selectedItems()
            projectName = [item.text().encode("ascii") for item in project]
            if projectName:
                Singleton.setProject(str(projectName[0], 'utf-8'))
                try:
                    projectDb = dbconnection.getCollection(Singleton.getProject())
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
                    self.main.setWindowTitle("BEAT | "+Singleton.getProject())
                except Exception as e:
                    x = pop.errorDialog(self.projectTab,str(e),"Error")
                    x.exec_()