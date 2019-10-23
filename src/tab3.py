from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os, xmltodict, xmlschema
from singleton import Singleton


class Tab3(QtWidgets.QWidget):
    def __init__(self, parent, main):
        QtWidgets.QWidget.__init__(self, parent)

        horizontalLayout = QtWidgets.QHBoxLayout(self)
        horizontalLayout.setObjectName("horizontalLayout")
        groupBox_3 = QtWidgets.QGroupBox(self)
        groupBox_3.setGeometry(QtCore.QRect(10, 10, 181, 550))
        groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        groupBox_3.setObjectName("groupBox_3")
        verticalLayoutWidget_2 = QtWidgets.QWidget(groupBox_3)
        verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 161, 471))
        verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        verticalLayout_2 = QtWidgets.QVBoxLayout(verticalLayoutWidget_2)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.setSpacing(20)
        verticalLayout_2.setObjectName("verticalLayout_2")
        lineEdit = QtWidgets.QLineEdit(verticalLayoutWidget_2)
        lineEdit.setObjectName("lineEdit")
        lineEdit.addAction(QtGui.QIcon("resources/search.png"), QtWidgets.QLineEdit.LeadingPosition)
        verticalLayout_2.addWidget(lineEdit)
        self.listWidget = QtWidgets.QListWidget(verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        verticalLayout_2.addWidget(self.listWidget)
        pushButton_7 = QtWidgets.QPushButton(verticalLayoutWidget_2)
        pushButton_7.setObjectName("pushButton_7")
        pushButton_7.clicked.connect(self.createPlugin)
        verticalLayout_2.addWidget(pushButton_7)
        horizontalLayout.addWidget(groupBox_3)
    
        DetailedPluginView = QtWidgets.QFrame(self)
        DetailedPluginView.setLayoutDirection(QtCore.Qt.LeftToRight)
        DetailedPluginView.setFrameShape(QtWidgets.QFrame.WinPanel)
        DetailedPluginView.setFrameShadow(QtWidgets.QFrame.Sunken)
        DetailedPluginView.setLineWidth(3)
        DetailedPluginView.setObjectName("DetailedPluginView")
        verticalLayout = QtWidgets.QVBoxLayout(DetailedPluginView)
        verticalLayout.setObjectName("verticalLayout")
        LabelDetailedPLuginView = QtWidgets.QLabel(DetailedPluginView)
        LabelDetailedPLuginView.setTextFormat(QtCore.Qt.RichText)
        LabelDetailedPLuginView.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        LabelDetailedPLuginView.setObjectName("LabelDetailedPLuginView")
        verticalLayout.addWidget(LabelDetailedPLuginView)
        DPVContents = QtWidgets.QFrame(DetailedPluginView)
        DPVContents.setEnabled(True)
        DPVContents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        DPVContents.setFrameShadow(QtWidgets.QFrame.Raised)
        DPVContents.setObjectName("DPVContents")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(DPVContents)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        DPVLeft = QtWidgets.QFormLayout()
        DPVLeft.setObjectName("DPVLeft")
        LabelDPVPluginStructure = QtWidgets.QLabel(DPVContents)
        LabelDPVPluginStructure.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        LabelDPVPluginStructure.setObjectName("LabelDPVPluginStructure")
        DPVLeft.setWidget(0, QtWidgets.QFormLayout.LabelRole, LabelDPVPluginStructure)
        self.DPVPluginStructure = QtWidgets.QLineEdit(DPVContents)
        self.DPVPluginStructure.setAlignment(QtCore.Qt.AlignCenter)
        self.DPVPluginStructure.setObjectName("DPVPluginStructure")
        DPVLeft.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DPVPluginStructure)
        LabelDPVPluginDataSet = QtWidgets.QLabel(DPVContents)
        LabelDPVPluginDataSet.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        LabelDPVPluginDataSet.setObjectName("LabelDPVPluginDataSet")
        DPVLeft.setWidget(1, QtWidgets.QFormLayout.LabelRole, LabelDPVPluginDataSet)
        self.DPVPluginDataSet = QtWidgets.QLineEdit(DPVContents)
        self.DPVPluginDataSet.setAlignment(QtCore.Qt.AlignCenter)
        self.DPVPluginDataSet.setObjectName("DPVPluginDataSet")
        DPVLeft.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DPVPluginDataSet)
        LabelDPVPluginName = QtWidgets.QLabel(DPVContents)
        LabelDPVPluginName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        LabelDPVPluginName.setObjectName("LabelDPVPluginName")
        DPVLeft.setWidget(2, QtWidgets.QFormLayout.LabelRole, LabelDPVPluginName)
        self.DPVPluginName = QtWidgets.QLineEdit(DPVContents)
        self.DPVPluginName.setAlignment(QtCore.Qt.AlignCenter)
        self.DPVPluginName.setObjectName("DPVPluginName")
        DPVLeft.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DPVPluginName)
        LabelDPVPLuginDescription = QtWidgets.QLabel(DPVContents)
        LabelDPVPLuginDescription.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        LabelDPVPLuginDescription.setObjectName("LabelDPVPLuginDescription")
        DPVLeft.setWidget(3, QtWidgets.QFormLayout.LabelRole, LabelDPVPLuginDescription)
        self.DPVPluginDescription = QtWidgets.QTextEdit(DPVContents)
        self.DPVPluginDescription.setObjectName("DPVPluginDescription")
        DPVLeft.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DPVPluginDescription)
        LabelDPVOutputField = QtWidgets.QLabel(DPVContents)
        LabelDPVOutputField.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        LabelDPVOutputField.setObjectName("LabelDPVOutputField")
        DPVLeft.setWidget(4, QtWidgets.QFormLayout.LabelRole, LabelDPVOutputField)
        DPVDefaultOutputField = QtWidgets.QComboBox(DPVContents)
        DPVDefaultOutputField.setCurrentText("")
        DPVDefaultOutputField.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        DPVDefaultOutputField.setObjectName("DPVDefaultOutputField")
        DPVLeft.setWidget(4, QtWidgets.QFormLayout.FieldRole, DPVDefaultOutputField)
        LabelDPVPointOfInterest = QtWidgets.QLabel(DPVContents)
        LabelDPVPointOfInterest.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        LabelDPVPointOfInterest.setObjectName("LabelDPVPointOfInterest")
        DPVLeft.setWidget(5, QtWidgets.QFormLayout.LabelRole, LabelDPVPointOfInterest)
        self.DVPPointOfInterest = QtWidgets.QTextBrowser(DPVContents)
        self.DVPPointOfInterest.setObjectName("DVPPointOfInterest")
        DPVLeft.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DVPPointOfInterest)
        horizontalLayout_2.addLayout(DPVLeft)
        DPVRight = QtWidgets.QVBoxLayout()
        DPVRight.setContentsMargins(-1, -1, -1, 0)
        DPVRight.setObjectName("DPVRight")
        ButtonDPVPluginStructure = QtWidgets.QPushButton(DPVContents)
        ButtonDPVPluginStructure.clicked.connect(self.BrowseStruct)
        ButtonDPVPluginStructure.setObjectName("ButtonDPVPluginStructure")
        DPVRight.addWidget(ButtonDPVPluginStructure, 0, QtCore.Qt.AlignTop)
        ButtonDPVBDataset = QtWidgets.QPushButton(DPVContents)
        ButtonDPVBDataset.clicked.connect(self.BrowseDataSet)
        ButtonDPVBDataset.setObjectName("ButtonDPVBDataset")
        DPVRight.addWidget(ButtonDPVBDataset)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        DPVRight.addItem(spacerItem1)
        horizontalLayout_2.addLayout(DPVRight)
        verticalLayout.addWidget(DPVContents)
        savingframe = QtWidgets.QHBoxLayout()
        savingframe.setSpacing(0)
        savingframe.setObjectName("savingframe")
        ButtonDeletePlugin = QtWidgets.QPushButton(DetailedPluginView)
        ButtonDeletePlugin.setObjectName("ButtonDeletePlugin")
        savingframe.addWidget(ButtonDeletePlugin)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        savingframe.addItem(spacerItem2)
        ButtonSavePlugin = QtWidgets.QPushButton(DetailedPluginView)
        ButtonSavePlugin.setObjectName("ButtonSavePlugin")
        savingframe.addWidget(ButtonSavePlugin, 0, QtCore.Qt.AlignLeft)
        verticalLayout.addLayout(savingframe)
        horizontalLayout.addWidget(DetailedPluginView)
        horizontalLayout.setStretch(0, 1)
        horizontalLayout.setStretch(1, 3)
    
        _translate = QtCore.QCoreApplication.translate

        LabelDetailedPLuginView.setText(_translate("self", "Detailed Plugin View"))
        LabelDPVPluginStructure.setText(_translate("self", "Plugin Structure"))
        LabelDPVPluginDataSet.setText(_translate("self", "Plugin Predetermined Data Set"))
        LabelDPVPluginName.setText(_translate("self", "Plugin Name"))
        LabelDPVPLuginDescription.setText(_translate("self", "Plugin Description"))
        LabelDPVOutputField.setText(_translate("self", "Default Output Field"))
        LabelDPVPointOfInterest.setText(_translate("self", "Points Of Interest"))
        ButtonDPVPluginStructure.setText(_translate("self", "Browse"))
        ButtonDPVBDataset.setText(_translate("self", "Browse"))
        ButtonDeletePlugin.setText(_translate("self", "Delete"))
        ButtonSavePlugin.setText(_translate("self", "Save"))
    
        groupBox_3.setTitle(_translate("MainWindow", "Plugin View"))
        pushButton_7.setText(_translate("MainWindow", "New"))
        self.searchPlugins()
        self.listWidget.itemSelectionChanged.connect(self.itemActivated)
    

    def BrowseStruct(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browse XML Schema", "",
                                                  "XML Schemas Files (*.xsd)", options=options)
        if fileName:
            self.DPVPluginStructure.setText(fileName)

    def BrowseDataSet(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browse XML File", "",
                                                  "XML Files (*.xml)", options=options)
        if fileName:
            self.DPVPluginDataSet.setText(fileName)

    def createPlugin(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Create New Plugin", "Name of Plugin:",
                                                         QtWidgets.QLineEdit.Normal, "")
        print(text)

    def deletePlugin(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        buttonReply = QtWidgets.QMessageBox.question(self, 'PyQt5 message', "Are you sure to delete Plugin ?",
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            self.DPVPluginStructure.setText("")
            self.DPVPluginDataSet.setText("")
            self.DPVPluginDescription.setText("")
            self.DPVPluginName.setText("")
            self.DVPPointOfInterest.setText("")

    def searchPlugins(self):
        self.listWidget.clear()
        for pl in Singleton.getPlugins():
            with open('plugins/%s' %pl) as fd:
                doc = xmltodict.parse(fd.read())
                i = doc["plugin"]["name"]
                self.listWidget.addItem(i)


    def itemActivated(self):
        plgSelect = self.listWidget.selectedItems()
        plgName = [item.text().encode("ascii") for item in plgSelect]
        for pl in Singleton.getPlugins():
            with open('plugins/%s' % pl) as fd:
                doc = xmltodict.parse(fd.read())
                if doc["plugin"]["name"] == plgName:
                    break
        xms = pl.split('.')[0]+'.xsd'
        schema = xmlschema.XMLSchema('plugins/%s' %xms)
        #print(pl.split('.')[0]+'.xsd')
        if plgName:
            self.DPVPluginName.setText(doc["plugin"]["name"])
            self.DPVPluginDescription.setText(doc["plugin"]["description"])
            self.DPVPluginDataSet.setText('plugins/%s' % pl)
            self.DPVPluginStructure.setText('plugins/%s'%xms )
            for i in doc["plugin"]["point_of_interest"]:
                lastText = self.DVPPointOfInterest.toPlainText()
                new = lastText + i["type"] + " " + i["name"] + "\n"
                self.DVPPointOfInterest.setText(new)

