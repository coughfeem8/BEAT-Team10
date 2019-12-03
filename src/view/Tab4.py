# Also known as tbe Point of Interest Tab
import xmlschema
from PyQt5 import QtCore, QtGui, QtWidgets


class Tab4(QtWidgets.QWidget):
    """UI for tab 4"""

    def __init__(self, parent):
        """Initializes tab 4 based on parent main window tab and sets up associated UI object"""
        QtWidgets.QWidget.__init__(self, parent)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 20, 201, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)

        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 179, 491))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 161, 451))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.addAction(QtGui.QIcon("resources/search.png"), QtWidgets.QLineEdit.LeadingPosition)
        self.verticalLayout_3.addWidget(self.lineEdit_4)

        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)

        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)

        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(219, 19, 551, 511))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)

        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 9, 531, 481))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 3, 1, 1, 1, QtCore.Qt.AlignRight)

        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget_3)

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())

        self.frame_3.setSizePolicy(self.sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 531, 365))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)

        self.sizePolicy_2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.sizePolicy_2.setHorizontalStretch(0)
        self.sizePolicy_2.setVerticalStretch(0)
        self.sizePolicy_2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())

        self.label_6.setSizePolicy(self.sizePolicy_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 2, QtCore.Qt.AlignTop)

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 2)

        _translate = QtCore.QCoreApplication.translate

        self.groupBox_5.setTitle(_translate("MainWindow", "Point of Interest"))
        self.pushButton_11.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Detail Point of Interest View"))
        self.label_12.setText(_translate("MainWindow", "Plugin"))
        self.label_13.setText(_translate("MainWindow", "Point of Interest Type"))
