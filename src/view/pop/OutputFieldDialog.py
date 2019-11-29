from PyQt5 import QtCore, QtGui, QtWidgets
from view.pop import PopUpDialog


class OutputFieldDialog(PopUpDialog.PopUpDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)

        self.setObjectName("Dialog")
        self.resize(402, 381)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(150, 10, 241, 41))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 101, 41))
        self.pushButton.clicked.connect(self.save_text)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 320, 101, 41))
        self.pushButton_2.clicked.connect(self.clear_text)
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(150, 60, 241, 141))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 210, 241, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 20, 67, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 67, 17))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.returnVal = ""

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("Dialog", "Output Field View"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Generate"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Description"))
        self.label_3.setText(_translate("Dialog", "Location"))
