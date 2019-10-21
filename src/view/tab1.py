from PyQt5 import QtCore, QtGui, QtWidgets


class Tab1(QtWidgets.QWidget):
    def __init__(self, parent, mainA):
        QtWidgets.QWidget.__init__(self, parent)

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)

        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 181, 550))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 161, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.addAction(QtGui.QIcon("resources/search.png"), QtWidgets.QLineEdit.LeadingPosition)
        self.verticalLayout_2.addWidget(self.lineEdit)

        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.verticalLayout_2.addWidget(self.listWidget)

        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.groupBox_4 = QtWidgets.QGroupBox(self)
        self.groupBox_4.setGeometry(QtCore.QRect(200, 10, 581, 550))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)

        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 561, 510))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget()

        self.gridLayout_2.addWidget(self.tableWidget, 3, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setEnabled(False)
        self.gridLayout_2.addWidget(self.pushButton_8, 2, 2, 1, 1)

        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 1, 1, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 4, 0, 1, 1)

        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setEnabled(False)
        self.gridLayout_2.addWidget(self.pushButton_10, 4, 2, 1, 1)

        _translate = QtCore.QCoreApplication.translate

        self.groupBox_3.setTitle(_translate("MainWindow", "Project View"))
        self.pushButton_7.setText(_translate("MainWindow", "New"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Detailed Project View"))
        self.label_8.setText(_translate("MainWindow", "Project Description"))
        self.pushButton_8.setText(_translate("MainWindow", "Browse"))
        self.label_7.setText(_translate("MainWindow", "Project Name"))
        self.label_10.setText(_translate("MainWindow", "Binary File Properties"))
        self.label_9.setText(_translate("MainWindow", "Binary File Path"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
