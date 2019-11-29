from PyQt5 import QtCore, QtGui, QtWidgets
from view.pop import PopUpDialog


class AnalysisResultDialog(PopUpDialog.PopUpDialog):
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
        self.pushButton.clicked.connect(self.save_text)
        self.pushButton.setObjectName("pushButton")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 81, 21))
        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(268, 200, 101, 31))
        self.pushButton_2.clicked.connect(self.save_text)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 170, 91, 31))
        self.pushButton_3.clicked.connect(self.save_text)
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
