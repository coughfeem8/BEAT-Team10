from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os

from src import pop

class Tab1(QtWidgets.QWidget):
    def __init__(self, parent, main):
        QtWidgets.QWidget.__init__(self, parent)

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

        tableWidget = self.fillBnryProp()

        gridLayout_2.addWidget(tableWidget, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.openComment)

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
        pushButton_10 = QtWidgets.QPushButton(gridLayoutWidget_2)
        pushButton_10.setObjectName("pushButton_10")
        pushButton_10.clicked.connect(self.SaveProject)
        gridLayout_2.addWidget(pushButton_10, 4, 2, 1, 1)

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
        pushButton_10.setText(_translate("MainWindow", "Save"))

    def fillBnryProp(self):
        properties = ["OS", "Binary Type", "Machine", "Class", "Bits", "Language", "Canary", "Cripto", "Nx", "Pic",
                      "Relocs"
            , "Relro", "Stripped"]

        tableWidget = QtWidgets.QTableWidget()
        tableWidget.setObjectName("tableWidget")
        tableWidget.setColumnCount(2)
        tableWidget.setRowCount(13)
        tableWidget.horizontalHeader().hide()
        tableWidget.verticalHeader().hide()
        tableWidget.horizontalHeader().setStretchLastSection(True)

        bolds = QtGui.QFont()
        QtGui.QFont.setBold(bolds, True)
        for x in range(len(properties)):
            item = QtWidgets.QTableWidgetItem(properties[x])
            item.setFont(bolds)
            tableWidget.setItem(x, 0, item)

        return tableWidget

    def BrowseBnryFiles(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browse Binary File", "",
                                                  "All Files (*);;Binary Files (*.exe,*.elf)", options=options)
        if fileName:
            self.lineEdit_3.setText(fileName)

    def SaveProject(self):
        file = open("projectsTest/"+self.nameProject+".txt", 'w')
        file.write(self.lineEdit_2.text()+"\n")
        file.write(self.textEdit_2.toPlainText()+"\n")
        file.write(self.lineEdit_3.text()+"\n")
        file.close()

    def createProject(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Create New Project", "Name of Project:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            self.lineEdit_2.setText("")
            self.textEdit_2.setText("")
            self.lineEdit_3.setText("")
            file = open("projectsTest/"+text+".txt", 'w')
            self.nameProject = text
            self.listWidget.addItem(text)
            item = self.listWidget.findItems(text, QtCore.Qt.MatchExactly)
            self.listWidget.setCurrentItem(item[0])
            file.close()

    def itemActivated_event(self):
        project = self.listWidget.selectedItems()
        projectName = [item.text().encode("ascii") for item in project]
        self.nameProject = str(projectName[0], 'utf-8')
        try:
            file = open("projectsTest/"+self.nameProject+".txt", 'r')
            i=0
            for line in file:
                #print(line)
                if i == 0:
                    self.lineEdit_2.setText(line)
                elif i == 2:
                    self.textEdit_2.setPlainText(line)
                elif i == 1:
                    self.lineEdit_3.setText(line)
                i=+1
        except Exception as e:
            print(e)

    def searchProjects(self):
        for file in os.listdir("./projectsTest"):
            if file.endswith(".txt"):
                self.listWidget.addItem(file[:-4])

    def deleteProject(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        if self.nameProject != "":
            buttonReply = QtWidgets.QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                os.remove("./projectsTest/"+self.nameProject+".txt")
                self.lineEdit_2.setText("")
                self.textEdit_2.setText("")
                self.lineEdit_3.setText("")
                item = self.listWidget.findItems(self.nameProject,QtCore.Qt.MatchExactly)
                self.listWidget.removeItemWidget(item[0])
        else:
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()

    def openComment(self):
        popUp = pop.commentDialog(self)
        text = popUp.exec_()
        print(text)