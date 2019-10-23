from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os


class plugin_tab_controller:

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab

    def establish_connections(self):
        self.plugin_tab.pushButton_7.clicked.connect(self.createPlugin)
        self.plugin_tab.ButtonDPVPluginStructure.clicked.connect(self.BrowseStruct)
        self.plugin_tab.ButtonDPVBDataset.clicked.connect(self.BrowseDataSet)
        print("test")

    def BrowseStruct(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab, "Browse Binary File", "",
                                                            "All Files (*);;Binary Files (*.exe,*.elf)",
                                                            options=options)
        if fileName:
            self.plugin_tab.DPVPluginStructure.setText(fileName)

    def BrowseDataSet(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab, "Browse Binary File", "",
                                                            "All Files (*);;Binary Files (*.exe,*.elf)",
                                                            options=options)
        if fileName:
            self.plugin_tab.DPVPluginDataSet.setText(fileName)

    def createPlugin(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self.plugin_tab, "Create New Plugin", "Name of Plugin:",
                                                         QtWidgets.QLineEdit.Normal, "")
        print(text)

    def deletePlugin(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        buttonReply = QtWidgets.QMessageBox.question(self.plugin_tab, 'PyQt5 message',
                                                     "Are you sure to delete Plugin ?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            self.plugin_tab.DPVPluginStructure.setText("")
            self.plugin_tab.DPVPluginDataSet.setText("")
            self.plugin_tab.DPVPluginDescription.setText("")
            self.plugin_tab.DPVPluginName.setText("")
            self.plugin_tab.DVPPointOfInterest.setText("")
