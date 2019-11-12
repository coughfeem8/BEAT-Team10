from PyQt5 import QtCore, QtGui, QtWidgets
import xmlschema, xmltodict

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

class addPOIDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self,parent)
        self.resize(400, 512)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(19, 9, 361, 141))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 281, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(300, 50, 51, 21))
        self.pushButton.setObjectName("pushButton")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox_2.setGeometry(QtCore.QRect(10, 90, 341, 32))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 160, 361, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 54, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 251, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 80, 121, 25))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 120, 331, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 81, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 40, 221, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 80, 221, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 81, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 120, 221, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox_3.setGeometry(QtCore.QRect(10, 290, 341, 32))
        self.buttonBox_3.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_3.setObjectName("buttonBox_3")



        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Add Point of Interest"))
        self.groupBox.setTitle(_translate("Dialog", "Add POI in bulk"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.groupBox_2.setTitle(_translate("Dialog", "Add single POI"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Type"))
        self.comboBox.addItem("Function")
        self.comboBox.addItem("String")
        self.groupBox_3.setTitle(_translate("Dialog", "Attributes"))
        self.label_3.setText(_translate("Dialog", "Parameters"))
        self.label_4.setText(_translate("Dialog", "Return Type"))
        self.label_5.setText(_translate("Dialog", "Output"))


        self.pois = []
        self.comboBox.currentIndexChanged.connect(lambda x: self.checkType(self.comboBox.currentText()))
        self.pushButton.clicked.connect(self.checkSchema)
        self.buttonBox_2.accepted.connect(self.accept)
        self.buttonBox_2.rejected.connect(self.reject)
        self.buttonBox_3.rejected.connect(self.reject)
        self.buttonBox_3.accepted.connect(self.acceptSingle)

    def checkType(self, type):
        if type == "String":
            self.groupBox_3.hide()
        else:
            self.groupBox_3.show()

    def checkSchema(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browse XML", "",
                                                            "XML Files (*.xml)", options=options)
        if fileName:
            schema = xmlschema.XMLSchema('./plugins/schema.xsd')
            try:
                schema.validate(fileName)
                self.lineEdit.setText(fileName)
                with open(fileName) as fd:
                    doc = xmltodict.parse(fd.read())
                    self.pois = doc["point_of_interest"]
            except Exception as e:
                x = errorDialog(self,str(e),"Error")
                x.exec_()

    def acceptSingle(self):
        if self.lineEdit_2.text() != "":
            if self.comboBox.currentText() == "String":
                doc = {"item":{"name":self.lineEdit_2.text(),"type":self.comboBox.currentText(),"attributes":{},"pythonOutput":""}}
                self.pois = doc
            elif self.comboBox.currentText() == "Function":
                doc = {"item":{"name":self.lineEdit_2.text(),"type":self.comboBox.currentText(),"attributes":{"parameters":self.lineEdit_3.text(),"retur":self.lineEdit_4.text()}
                               ,"pythonOutput":self.lineEdit_5.text()}}
                self.pois = doc
            self.accept()
        else:
            e = errorDialog(self, "Name must be filled", "Error")
            e.exec_()

    def exec_(self):
        super(addPOIDialog, self).exec_()
        return self.pois



class errorDialog(QtWidgets.QMessageBox):
    def __init__(self, parent, text, title):
        QtWidgets.QMessageBox.__init__(self, parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def exec_(self):
        super(errorDialog, self).exec_()
        return