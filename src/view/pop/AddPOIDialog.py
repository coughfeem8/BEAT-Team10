from PyQt5 import QtCore, QtGui, QtWidgets


class AddPOIDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)

        self.resize(402, 236)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 180, 168, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 381, 112))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setMaximumSize(QtCore.QSize(185, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Add Point of Interest"))
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("Dialog", "Add Point of Interest"))

        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton.clicked.connect(self.save_text)

        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_2.clicked.connect(self.clear_text)

        self.label.setText(_translate("Dialog", "Name"))

        self.label_4.setText(_translate("Dialog", "Output"))

        self.label_3.setText(_translate("Dialog", "Type"))

        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.comboBox_2.setItemText(0, _translate("Dialog", "String"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Function"))

        self.comboBox_2.currentIndexChanged.connect(self.get_current_index)

    def exec_(self):
        super(AddPOIDialog, self).exec_()
        return self.lineEdit.text(), self.lineEdit_2.text(), self.comboBox_2.currentText()

    def save_text(self):
        if self.lineEdit.text() is "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Name can't be empty.")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            retval = msg.exec_()
            return
        self.accept()

    def clear_text(self):
        self.accept()

    def get_current_index(self):
        print(self.comboBox_2.currentText())
