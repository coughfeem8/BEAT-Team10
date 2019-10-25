from PyQt5 import QtCore, QtGui, QtWidgets

class commentDialog(QtWidgets.QDialog):
    def __init__(self, parent, text):
        QtWidgets.QDialog.__init__(self, parent)
        self.setObjectName("Dialog")
        self.resize(402, 281)

        self.parent = parent

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 381, 161))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(text)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 101, 41))
        self.pushButton.clicked.connect(self.saveText)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 220, 101, 41))
        self.pushButton_2.clicked.connect(self.clearText)
        self.pushButton_2.setObjectName("pushButton_2")

        self.returnVal = ""

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Comment View"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))

    def exec_(self):
        super(commentDialog, self).exec_()
        return self.returnVal

    def saveText(self):
        self.returnVal = self.textEdit.toPlainText()
        self.accept()

    def clearText(self):
        self.returnVal = ""
        self.accept()


class analysisResultDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)

        self.setObjectName("Dialog")
        self.resize(402, 467)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 361, 41))
        self.textEdit.setObjectName("textEdit")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-1, 219, 421, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 0, 141, 31))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 40, 231, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 67, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 90, 231, 91))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 200, 91, 31))
        self.pushButton.clicked.connect(self.saveText)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 81, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(268, 200, 101, 31))
        self.pushButton_2.clicked.connect(self.saveText)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 170, 91, 31))
        self.pushButton_3.clicked.connect(self.saveText)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(140, 50, 121, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(140, 80, 121, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(140, 110, 131, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(150, 140, 101, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.returnVal = ""

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Analysis Result View"))
        self.label.setText(_translate("Dialog", "Analysis Result Area"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.pushButton.setText(_translate("Dialog", "Delete"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))
        self.pushButton_3.setText(_translate("Dialog", "New"))
        self.label_4.setText(_translate("Dialog", "Analysis Result A"))
        self.label_5.setText(_translate("Dialog", "Analysis Result B"))
        self.label_6.setText(_translate("Dialog", "Analysis Result C"))
        self.label_7.setText(_translate("Dialog", "..."))

    def exec_(self):
        super(analysisResultDialog, self).exec_()
        return self.returnVal

    def saveText(self):
        self.returnVal = self.textEdit.toPlainText()
        self.accept()

    def clearText(self):
            self.returnVal = ""
            self.accept()

class outputFieldDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)

        self.setObjectName("Dialog")
        self.resize(402, 381)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(150, 10, 241, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 101, 41))
        self.pushButton.clicked.connect(self.saveText)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 320, 101, 41))
        self.pushButton_2.clicked.connect(self.clearText)
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

    def exec_(self):
        super(outputFieldDialog, self).exec_()
        return self.returnVal

    def saveText(self):
        self.returnVal = self.textEdit.toPlainText()
        self.accept()

    def clearText(self):
        self.returnVal = ""
        self.accept()