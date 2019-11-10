from model import plugin, dbconnection
from model.singleton import Singleton
from view import pop
from PyQt5 import QtWidgets, QtCore

class plugin_tab_controller:

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab
        self.plugin = ""

    def establish_connections(self):
        self.plugin_tab.pushButton_7.clicked.connect(self.createPlugin)
        self.plugin_tab.listWidget.itemSelectionChanged.connect(self.itemActivated)

    def establish_calls(self):
        self.setPlugins()

    def setPlugins(self):
        for pl in plugin.getInstalled():
            self.plugin_tab.listWidget.addItem(pl)

    def createPlugin(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self.plugin_tab, "Create New Plugin", "Name of Plugin:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            dbnames = dbconnection.getCollection("plugin")
            if text in dbnames:
                x= pop.errorDialog(self.plugin_tab,"Plugin with that name already exists","Error Creating Plugin")
                x.exec_()
                return
            self.plugin_tab.DPVPluginDescription.setText("")
            self.plugin_tab.DPVPluginName.setText(text)
            self.plugin_tab.DVPPointOfInterest.setText("")
            self.plugin_tab.DPVDefaultOutputField.setText("")
            self.plugin_tab.listWidget.addItem(text)
            item = self.plugin_tab.listWidget.findItems(text, QtCore.Qt.MatchExactly)
            self.plugin_tab.listWidget.setCurrentItem(item[0])

    def savePlugin(self):
        pluginDB = dbconnection.getCollection("plugin")
        plgCllc = pluginDB[self.plugin_tab.DPVPluginName.text()]
        info = {"name": self.plugin_tab.DPVPluginName.text(), "desc": self.plugin_tab.DPVPluginDescription.text(),
                "poi": "", "output": self.plugin_tab.DPVDefaultOutputField.text()}
        plgCllc.insert(info, check_keys=False)
        x = pop.errorDialog(self.plugin_tab,"Plugin Saved", "Save Plugin")
        x.exec_()

    def deletePlugin(self):
        if self.plugin != "":
            buttonReply = QtWidgets.QMessageBox.question(self.plugin_tab, 'PyQt5 message',
                                                         "Do you like to erase Plugin %s ?" % self.plugin,
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                         QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                projectDb = dbconnection.getCollection("plugin")
                projectDb.drop_collection(self.plugin)
                self.plugin = ""
                self.plugin_tab.DPVPluginDescription.setText("")
                self.plugin_tab.DPVPluginName.setText("")
                self.plugin_tab.DVPPointOfInterest.setText("")
                self.plugin_tab.DPVDefaultOutputField.setText("")
                listItems = self.plugin_tab.listWidget.selectedItems()
                if not listItems: return
                for item in listItems:
                    self.plugin_tab.listWidget.takeItem(self.plugin_tab.listWidget.row(item))
        else:
            x = pop.errorDialog(self.plugin_tab,"Please select a plugin", "Error")
            x.exec_()

    def itemActivated(self):
        if self.plugin_tab.listWidget.count() != 0:
            plugin = self.plugin_tab.listWidget.selectedItems()
            pluginName = [item.text().encode("ascii") for item in plugin]
            if pluginName:
                try:
                    self.plugin = pluginName
                    pluginDB = dbconnection.getCollection("plugin")
                    plgCllc = pluginDB[pluginName]
                    cursor = plgCllc.find()
                    for pl in cursor:
                        print(pl["name"])
                        self.plugin_tab.DPVPluginName.setText(pl["name"])
                        self.plugin_tab.DPVPluginDescription.setText(pl["desc"])
                        self.plugin_tab.DPVDefaultOutputField.setText(pl["output"]["functionSource"])
                        for i in pl["poi"]["item"]:
                            lastText = self.plugin_tab.DVPPointOfInterest.toPlainText()
                            new = lastText + i["type"] + " " + i["name"] + "\n"
                            self.plugin_tab.DVPPointOfInterest.setText(new)
                except Exception as e:
                    x = pop.errorDialog(self.plugin_tab,str(e),"Error")
                    x.exec_()