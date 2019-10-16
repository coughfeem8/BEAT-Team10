from PyQt5 import QtCore, QtGui, QtWidgets
import r2pipe
import pymongo
from singleton import Singleton


class Tab1(QtWidgets.QWidget):
    def __init__(self, parent, mainA):
        QtWidgets.QWidget.__init__(self, parent)
        global mainWin
        mainWin = mainA
        global activeProject
        global saved
        saved = False
        self.nameProject = ""

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 181, 550))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 161, 471))
        verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        verticalLayout_2 = QtWidgets.QVBoxLayout(verticalLayoutWidget_2)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.setSpacing(20)
        verticalLayout_2.setObjectName("verticalLayout_2")
        lineEdit = QtWidgets.QLineEdit(verticalLayoutWidget_2)
        lineEdit.setObjectName("lineEdit")
        lineEdit.addAction(QtGui.QIcon("resources/search.png"), QtWidgets.QLineEdit.LeadingPosition)
        verticalLayout_2.addWidget(lineEdit)
        self.listWidget = QtWidgets.QListWidget(verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.itemSelectionChanged.connect(self.itemActivated_event)
        verticalLayout_2.addWidget(self.listWidget)
        pushButton_7 = QtWidgets.QPushButton(verticalLayoutWidget_2)
        pushButton_7.setObjectName("pushButton_7")
        pushButton_7.clicked.connect(self.createProject)
        verticalLayout_2.addWidget(pushButton_7)

        self.searchProjects()

        groupBox_4 = QtWidgets.QGroupBox(self)
        groupBox_4.setGeometry(QtCore.QRect(200, 10, 581, 550))
        groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        groupBox_4.setObjectName("groupBox_4")
        gridLayoutWidget_2 = QtWidgets.QWidget(groupBox_4)
        gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 561, 510))
        gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        gridLayout_2 = QtWidgets.QGridLayout(gridLayoutWidget_2)
        gridLayout_2.setContentsMargins(0, 0, 0, 0)
        gridLayout_2.setSpacing(20)
        gridLayout_2.setObjectName("gridLayout_2")
        label_8 = QtWidgets.QLabel(gridLayoutWidget_2)
        label_8.setObjectName("label_8")
        gridLayout_2.addWidget(label_8, 1, 0, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget()
        self.fillBnryPropEmpty()

        gridLayout_2.addWidget(self.tableWidget, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.BrowseBnryFiles)

        gridLayout_2.addWidget(self.pushButton_8, 2, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(gridLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        gridLayout_2.addWidget(self.textEdit_2, 1, 1, 1, 1)
        label_7 = QtWidgets.QLabel(gridLayoutWidget_2)
        label_7.setObjectName("label_7")
        gridLayout_2.addWidget(label_7, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(gridLayoutWidget_2)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")

        gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        label_10 = QtWidgets.QLabel(gridLayoutWidget_2)
        label_10.setObjectName("label_10")
        gridLayout_2.addWidget(label_10, 3, 0, 1, 1)
        label_9 = QtWidgets.QLabel(gridLayoutWidget_2)
        label_9.setObjectName("label_9")
        gridLayout_2.addWidget(label_9, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(gridLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        pushButton_9 = QtWidgets.QPushButton(gridLayoutWidget_2)
        pushButton_9.clicked.connect(self.deleteProject)
        pushButton_9.setObjectName("pushButton_9")

        gridLayout_2.addWidget(pushButton_9, 4, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(gridLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.SaveProject)
        gridLayout_2.addWidget(self.pushButton_10, 4, 2, 1, 1)

        self.pushButton_10.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.lineEdit_2.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)

        _translate = QtCore.QCoreApplication.translate

        self.groupBox_3.setTitle(_translate("MainWindow", "Project View"))
        pushButton_7.setText(_translate("MainWindow", "New"))
        groupBox_4.setTitle(_translate("MainWindow", "Detailed Project View"))
        label_8.setText(_translate("MainWindow", "Project Description"))
        self.pushButton_8.setText(_translate("MainWindow", "Browse"))
        label_7.setText(_translate("MainWindow", "Project Name"))
        label_10.setText(_translate("MainWindow", "Binary File Properties"))
        label_9.setText(_translate("MainWindow", "Binary File Path"))
        pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))

    def fillBnryPropEmpty(self):
        properties = ["OS", "Arch", "Binary Type", "Machine", "Class", "Bits", "Language", "Canary", "Cripto", "Nx", "Pic",
                      "Endian"]

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(12)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        bolds = QtGui.QFont()
        QtGui.QFont.setBold(bolds, True)
        for x in range(len(properties)):
            item = QtWidgets.QTableWidgetItem(properties[x])
            empty = QtWidgets.QTableWidgetItem("")
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setFont(bolds)
            empty.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(x, 0, item)
            self.tableWidget.setItem(x, 1, empty)

    def fillBnryProp(self, r2BinInfo):
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["os"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["arch"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["core"]["type"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["machine"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["class"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["bits"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["lang"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["canary"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["crypto"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["nx"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem(str(r2BinInfo["bin"]["pic"]))
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem(r2BinInfo["bin"]["endian"])
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(11, 1, item)


    def BrowseBnryFiles(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browse Binary File", "",
                                                  "Binary Files (*.exe | *.elf | *.out)", options=options)

        if fileName:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            try:
                global r2BinInfo
                self.lineEdit_3.setText(fileName)
                rlocal = r2pipe.open(fileName)
                r2BinInfo = rlocal.cmdj("ij")

                if r2BinInfo["core"]["format"] == "any":
                    msg = QtWidgets.QMessageBox()
                    msg.setText("Error")
                    return
                if r2BinInfo["bin"]["arch"] != "x86":
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
        if self.lineEdit_3.text() != "":
            saved = False
            projectDb = mongoClient[self.nameProject]
            projInfo = projectDb["projectInfo"]
            info = {"ProjectName" : self.lineEdit_2.text(), "ProjectDescription" : self.textEdit_2.toPlainText(),
                    "BnyFilePath" : self.lineEdit_3.text()}
            insertInfo = projInfo.insert(info, check_keys=False)
            binInfo = projectDb["binaryInfo"]
            insertObj = binInfo.insert(r2BinInfo, check_keys=False)

            self.pushButton_10.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.lineEdit_2.setReadOnly(True)
            self.textEdit_2.setReadOnly(True)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Save Project")
            msg.setText("Project Saved")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please select a Binary File")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()


    def createProject(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Create New Project", "Name of Project:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            dbnames = mongoClient.list_database_names()
            if text in dbnames:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Project with that name already exists")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = msg.exec_()
                return
            activeProject = text
            self.lineEdit_2.setText(text)
            self.textEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.fillBnryPropEmpty()
            #self.parent.activeProj = text
            self.nameProject = text
            self.listWidget.addItem(text)
            item = self.listWidget.findItems(text, QtCore.Qt.MatchExactly)
            self.listWidget.setCurrentItem(item[0])
            self.setWindowTitle('Create Project')
            self.pushButton_10.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.textEdit_2.setReadOnly(False)

    def itemActivated_event(self):
        if self.listWidget.count() != 0:
            project = self.listWidget.selectedItems()
            projectName = [item.text().encode("ascii") for item in project]
            if projectName:
                self.nameProject = str(projectName[0], 'utf-8')
                try:
                    Singleton.setProject(self.nameProject)

                    projectDb = mongoClient[self.nameProject]
                    projInfo = projectDb["projectInfo"]
                    binInfo = projectDb["binaryInfo"]
                    cursor = projInfo.find()
                    for db in cursor:
                        self.textEdit_2.setPlainText(db['ProjectDescription'])
                        self.lineEdit_2.setText(db['ProjectName'])
                        self.lineEdit_3.setText(db['BnyFilePath'])
                        Singleton.setPath(db['BnyFilePath'])
                    cursorBin = binInfo.find()
                    for db in cursorBin:
                        self.fillBnryPropEmpty()
                        self.fillBnryProp(db)
                    if(saved):
                        mainWin.setWindowTitle("* "+self.nameProject)
                    else:
                        mainWin.setWindowTitle("BEAT | "+self.nameProject)
                    activeProject = self.nameProject

                except Exception as e:
                    print(e)
                    #print(1)

    def searchProjects(self):
        global mongoClient
        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        cursor = mongoClient.list_database_names()
        self.listWidget.clear()
        for db in cursor:
            if db not in ['admin', 'local', 'config']:
                self.listWidget.addItem(db)

    def deleteProject(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        if self.nameProject != "":
            buttonReply = QtWidgets.QMessageBox.question(self, 'PyQt5 message', "Do you like to erase Project %s ?" % self.nameProject,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:

                mongoClient.drop_database(self.nameProject)

                self.lineEdit_2.setText("")
                self.textEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.fillBnryPropEmpty()
                listItems = self.listWidget.selectedItems()
                if not listItems: return
                for item in listItems:
                    self.listWidget.takeItem(self.listWidget.row(item))

        else:
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
