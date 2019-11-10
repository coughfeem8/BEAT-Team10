from PyQt5 import QtCore, QtGui, QtWidgets


class Tab3(QtWidgets.QWidget):
    def __init__(self, parent, main):
        QtWidgets.QWidget.__init__(self, parent)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

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
        self.verticalLayout_2.addWidget(self.listWidget)

        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("self.pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.DetailedPluginView = QtWidgets.QFrame(self)
        self.DetailedPluginView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DetailedPluginView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.DetailedPluginView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DetailedPluginView.setLineWidth(3)
        self.DetailedPluginView.setObjectName("DetailedPluginView")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DetailedPluginView)
        self.verticalLayout.setObjectName("verticalLayout")

        self.LabelDetailedPLuginView = QtWidgets.QLabel(self.DetailedPluginView)
        self.LabelDetailedPLuginView.setTextFormat(QtCore.Qt.RichText)
        self.LabelDetailedPLuginView.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.LabelDetailedPLuginView.setObjectName("LabelDetailedPLuginView")
        self.verticalLayout.addWidget(self.LabelDetailedPLuginView)

        self.DPVContents = QtWidgets.QFrame(self.DetailedPluginView)
        self.DPVContents.setEnabled(True)
        self.DPVContents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DPVContents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DPVContents.setObjectName("DPVContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.DPVContents)

        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DPVLeft = QtWidgets.QFormLayout()
        self.DPVLeft.setObjectName("DPVLeft")

        self.LabelDPVPluginName = QtWidgets.QLabel(self.DPVContents)
        self.LabelDPVPluginName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.LabelDPVPluginName.setObjectName("LabelDPVPluginName")
        self.DPVLeft.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.LabelDPVPluginName)

        self.DPVPluginName = QtWidgets.QLineEdit(self.DPVContents)
        self.DPVPluginName.setAlignment(QtCore.Qt.AlignCenter)
        self.DPVPluginName.setObjectName("DPVPluginName")
        self.DPVLeft.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DPVPluginName)

        self.LabelDPVPLuginDescription = QtWidgets.QLabel(self.DPVContents)
        self.LabelDPVPLuginDescription.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.LabelDPVPLuginDescription.setObjectName("LabelDPVPLuginDescription")
        self.DPVLeft.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.LabelDPVPLuginDescription)

        self.DPVPluginDescription = QtWidgets.QTextEdit(self.DPVContents)
        self.DPVPluginDescription.setObjectName("DPVPluginDescription")
        self.DPVLeft.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DPVPluginDescription)

        self.LabelDPVOutputField = QtWidgets.QLabel(self.DPVContents)
        self.LabelDPVOutputField.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.LabelDPVOutputField.setObjectName("LabelDPVOutputField")
        self.DPVLeft.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.LabelDPVOutputField)

        self.DPVDefaultOutputField = QtWidgets.QLineEdit(self.DPVContents)
        self.DPVDefaultOutputField.setAlignment(QtCore.Qt.AlignCenter)
        self.DPVDefaultOutputField.setObjectName("DPVDefaultOutputField")
        self.DPVLeft.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.DPVDefaultOutputField)

        self.LabelDPVPointOfInterest = QtWidgets.QLabel(self.DPVContents)
        self.LabelDPVPointOfInterest.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.LabelDPVPointOfInterest.setObjectName("LabelDPVPointOfInterest")

        self.DPVLeft.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.LabelDPVPointOfInterest)
        self.DVPPointOfInterest = QtWidgets.QTextBrowser(self.DPVContents)
        self.DVPPointOfInterest.setObjectName("DVPPointOfInterest")
        self.DPVLeft.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DVPPointOfInterest)
        self.horizontalLayout_2.addLayout(self.DPVLeft)

        self.DPVRight = QtWidgets.QVBoxLayout()
        self.DPVRight.setContentsMargins(-1, -1, -1, 0)
        self.DPVRight.setObjectName("DPVRight")

        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.DPVRight.addItem(self.spacerItem1)

        self.horizontalLayout_2.addLayout(self.DPVRight)

        self.verticalLayout.addWidget(self.DPVContents)
        self.savingframe = QtWidgets.QHBoxLayout()
        self.savingframe.setSpacing(0)
        self.savingframe.setObjectName("savingframe")

        self.ButtonDeletePlugin = QtWidgets.QPushButton(self.DetailedPluginView)
        self.ButtonDeletePlugin.setObjectName("ButtonDeletePlugin")
        self.savingframe.addWidget(self.ButtonDeletePlugin)

        self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.savingframe.addItem(self.spacerItem2)

        self.ButtonSavePlugin = QtWidgets.QPushButton(self.DetailedPluginView)
        self.ButtonSavePlugin.setObjectName("ButtonSavePlugin")

        self.savingframe.addWidget(self.ButtonSavePlugin, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.savingframe)

        self.horizontalLayout.addWidget(self.DetailedPluginView)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        _translate = QtCore.QCoreApplication.translate

        self.LabelDetailedPLuginView.setText(_translate("self", "Detailed Plugin View"))

        self.LabelDPVPluginName.setText(_translate("self", "Plugin Name"))
        self.LabelDPVPLuginDescription.setText(_translate("self", "Plugin Description"))
        self.LabelDPVOutputField.setText(_translate("self", "Default Output Field"))
        self.LabelDPVPointOfInterest.setText(_translate("self", "Points Of Interest"))
        self.ButtonDeletePlugin.setText(_translate("self", "Delete"))
        self.ButtonSavePlugin.setText(_translate("self", "Save"))

        self.groupBox_3.setTitle(_translate("MainWindow", "Plugin View"))
        self.pushButton_7.setText(_translate("MainWindow", "New"))
