from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from model import plugin
import xmlschema


class plugin_tab_controller:

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab

    def establish_connections(self):
        self.plugin_tab.pushButton_7.clicked.connect(self.createPlugin)
        self.plugin_tab.ButtonDPVPluginStructure.clicked.connect(self.BrowseStruct)
        self.plugin_tab.ButtonDPVBDataset.clicked.connect(self.BrowseDataSet)
        self.plugin_tab.listWidget.itemSelectionChanged.connect(self.itemActivated)
        self.plugin_tab.lineEdit.textChanged.connect(
            lambda x: self.search_installed_plugins(self.plugin_tab.lineEdit.text()))

    def establish_calls(self):
        self.setPlugins()

    def setPlugins(self):
        for pl in plugin.getInstalledPlugins():
            self.plugin_tab.listWidget.addItem(pl)

    def BrowseStruct(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab, "Browse XML Schema", "",
                                                            "XML Schemas Files (*.xsd)", options=options)
        if fileName:
            self.plugin_tab.DPVPluginStructure.setText(fileName)

    def BrowseDataSet(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab, "Browse XML File", "",
                                                            "XML Files (*.xml)", options=options)
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

    def itemActivated(self):
        plgSelect = self.plugin_tab.listWidget.selectedItems()
        plgName = [item.text().encode("ascii") for item in plgSelect]
        doc = plugin.pluginConnection(plgName)
        pl = plugin.getPluginFile(plgName)
        xms = pl.split('.')[0] + '.xsd'
        schema = xmlschema.XMLSchema('plugins/%s' % xms)
        if plgName:
            self.plugin_tab.DPVPluginName.setText(doc["plugin"]["name"])
            self.plugin_tab.DPVPluginDescription.setText(doc["plugin"]["description"])
            self.plugin_tab.DPVPluginDataSet.setText('plugins/%s' % pl)
            self.plugin_tab.DPVPluginStructure.setText('plugins/%s' % xms)
            for i in doc["plugin"]["point_of_interest"]["item"]:
                lastText = self.plugin_tab.DVPPointOfInterest.toPlainText()
                new = lastText + i["type"] + " " + i["name"] + "\n"
                self.plugin_tab.DVPPointOfInterest.setText(new)

    def search_installed_plugins(self, text):
        if len(text) is not 0:
            search_result = self.plugin_tab.listWidget.findItems(text, QtCore.Qt.MatchContains)
            for item in range(self.plugin_tab.listWidget.count()):
                self.plugin_tab.listWidget.item(item).setHidden(True)
            for item in search_result:
                item.setHidden(False)
        else:
            for item in range(self.plugin_tab.listWidget.count()):
                self.plugin_tab.listWidget.item(item).setHidden(False)