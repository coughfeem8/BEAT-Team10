from PyQt5 import QtCore, QtGui, QtWidgets


class CommentDialog(QtWidgets.QDialog):
    def __init__(self, parent, text):
        QtWidgets.QDialog.__init__(self, parent)

        self.setObjectName("Dialog")
        self.resize(402, 281)

        self.parent = parent

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 381, 161))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(text)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 101, 41))
        self.pushButton.clicked.connect(self.save_text)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 220, 101, 41))
        self.pushButton_2.clicked.connect(self.clear_text)
        self.pushButton_2.setObjectName("pushButton_2")

        self.returnVal = ""

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("Dialog", "Comment View"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))

    def exec_(self):
        super(CommentDialog, self).exec_()
        return self.returnVal

    def save_text(self):
        self.returnVal = self.textEdit.toPlainText()
        self.accept()

    def clear_text(self):
        self.returnVal = ""
        self.accept()