import collections

import xmlschema
import xmltodict
from PyQt5 import QtCore, QtWidgets

from view.pop.ErrorDialog import ErrorDialog


class AddPOIDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
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
        self.comboBox.currentIndexChanged.connect(lambda x: self.check_type(self.comboBox.currentText()))
        self.pushButton.clicked.connect(self.check_schema)
        self.buttonBox_2.accepted.connect(self.accept)
        self.buttonBox_2.rejected.connect(self.reject)
        self.buttonBox_3.rejected.connect(self.reject)
        self.buttonBox_3.accepted.connect(self.accept_single)

    def check_type(self, poi_type):
        if poi_type == "String":
            self.groupBox_3.hide()
        else:
            self.groupBox_3.show()

    def check_schema(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browse XML", "",
                                                             "XML Files (*.xml)", options=options)
        if file_name:
            try:
                schema = xmlschema.XMLSchema('./model/plugin/schema.xsd')
                schema.validate(file_name)
                self.lineEdit.setText(file_name)
                with open(file_name) as fd:
                    doc = xmltodict.parse(fd.read())
                    self.pois = doc["point_of_interest"]
            except Exception as e:
                x = ErrorDialog(self, str(e), "Error")
                x.exec_()

    def accept_single(self):
        if self.lineEdit_2.text() != "":
            if self.comboBox.currentText() == "String":
                doc = {"item": [{"name": self.lineEdit_2.text(), "type": self.comboBox.currentText(), "attributes": {},
                                "pythonOutput": ""}]}
            elif self.comboBox.currentText() == "Function":
                doc = {"item": [{"name": self.lineEdit_2.text(), "type": self.comboBox.currentText(),
                                "attributes": {"parameters": self.lineEdit_3.text(), "retur": self.lineEdit_4.text()}
                    , "pythonOutput": self.lineEdit_5.text()}]}
            self.pois = doc
            self.accept()
        else:
            e = ErrorDialog(self, "Name must be filled", "Error")
            e.exec_()

    def exec_(self):
        super(AddPOIDialog, self).exec_()
        return self.pois
