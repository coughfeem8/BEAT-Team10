from PyQt5 import QtCore, QtGui, QtWidgets

def fillTab1(self):
    ProjectTab = QtWidgets.QWidget()
    ProjectTab.setObjectName("ProjectTab")

    groupBox_3 = QtWidgets.QGroupBox(ProjectTab)
    groupBox_3.setGeometry(QtCore.QRect(10, 10, 181, 550))
    groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
    groupBox_3.setObjectName("groupBox_3")
    verticalLayoutWidget_2 = QtWidgets.QWidget(groupBox_3)
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
    listWidget = QtWidgets.QListWidget(verticalLayoutWidget_2)
    listWidget.setObjectName("listWidget")
    listWidget.addItem("Project A")
    listWidget.addItem("Project B")
    listWidget.addItem("Project C")
    listWidget.addItem("Project D")
    verticalLayout_2.addWidget(listWidget)
    pushButton_7 = QtWidgets.QPushButton(verticalLayoutWidget_2)
    pushButton_7.setObjectName("pushButton_7")
    verticalLayout_2.addWidget(pushButton_7)

    groupBox_4 = QtWidgets.QGroupBox(ProjectTab)
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

    tableWidget = fillBnryProp()

    gridLayout_2.addWidget(tableWidget, 3, 1, 1, 1)
    pushButton_8 = QtWidgets.QPushButton(gridLayoutWidget_2)
    pushButton_8.setObjectName("pushButton_8")
    #pushButton_8.clicked.connect(openFileNameDialog(self))
    gridLayout_2.addWidget(pushButton_8, 2, 2, 1, 1)
    textEdit_2 = QtWidgets.QTextEdit(gridLayoutWidget_2)
    textEdit_2.setObjectName("textEdit_2")
    gridLayout_2.addWidget(textEdit_2, 1, 1, 1, 1)
    label_7 = QtWidgets.QLabel(gridLayoutWidget_2)
    label_7.setObjectName("label_7")
    gridLayout_2.addWidget(label_7, 0, 0, 1, 1)
    lineEdit_3 = QtWidgets.QLineEdit(gridLayoutWidget_2)
    lineEdit_3.setObjectName("lineEdit_3")
    gridLayout_2.addWidget(lineEdit_3, 2, 1, 1, 1)
    label_10 = QtWidgets.QLabel(gridLayoutWidget_2)
    label_10.setObjectName("label_10")
    gridLayout_2.addWidget(label_10, 3, 0, 1, 1)
    label_9 = QtWidgets.QLabel(gridLayoutWidget_2)
    label_9.setObjectName("label_9")
    gridLayout_2.addWidget(label_9, 2, 0, 1, 1)
    lineEdit_2 = QtWidgets.QLineEdit(gridLayoutWidget_2)
    lineEdit_2.setObjectName("lineEdit_2")
    gridLayout_2.addWidget(lineEdit_2, 0, 1, 1, 1)
    pushButton_9 = QtWidgets.QPushButton(gridLayoutWidget_2)
    pushButton_9.setObjectName("pushButton_9")
    gridLayout_2.addWidget(pushButton_9, 4, 0, 1, 1)
    pushButton_10 = QtWidgets.QPushButton(gridLayoutWidget_2)
    pushButton_10.setObjectName("pushButton_10")
    gridLayout_2.addWidget(pushButton_10, 4, 2, 1, 1)

    _translate = QtCore.QCoreApplication.translate

    groupBox_3.setTitle(_translate("MainWindow", "Project View"))
    pushButton_7.setText(_translate("MainWindow", "New"))
    groupBox_4.setTitle(_translate("MainWindow", "Detailed Project View"))
    label_8.setText(_translate("MainWindow", "Project Description"))
    pushButton_8.setText(_translate("MainWindow", "Browse"))
    label_7.setText(_translate("MainWindow", "Project Name"))
    label_10.setText(_translate("MainWindow", "Binary FIle Properties"))
    label_9.setText(_translate("MainWindow", "Binary File Path"))
    pushButton_9.setText(_translate("MainWindow", "Delete"))
    pushButton_10.setText(_translate("MainWindow", "Save"))
    
    return ProjectTab


def fillBnryProp():
    properties = ["OS", "Binary Type", "Machine", "Class", "Bits", "Language", "Canary", "Cripto"]

    tableWidget = QtWidgets.QTableWidget()
    tableWidget.setObjectName("tableWidget")
    tableWidget.setColumnCount(2)
    tableWidget.setRowCount(8)
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

@QtCore.pyqtSlot()
def openFileNameDialog(self):
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
    if fileName:
        print(fileName)