from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from model import Plugin, DBConnection
from view.pop.ErrorDialog import ErrorDialog


class PluginTabController:

    pluginSignal = QtCore.pyqtSignal()

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab
        self.plugin = ""

    def establish_connections(self):
        self.plugin_tab.pushButton_7.clicked.connect(self.createPlugin)
        self.plugin_tab.ButtonSavePlugin.clicked.connect(self.savePlugin)
        self.plugin_tab.ButtonDeletePlugin.clicked.connect(self.deletePlugin)
        self.plugin_tab.listWidget.itemSelectionChanged.connect(self.itemActivated)
        self.plugin_tab.lineEdit.textChanged.connect(
            lambda x: self.search_installed_plugins(self.plugin_tab.lineEdit.text()))

    def establish_calls(self):
        self.set_plugins()

    def set_plugins(self):
        self.plugin_tab.listWidget.clear()
        for pl in Plugin.get_installed_plugins():
            self.plugin_tab.listWidget.addItem(pl)

    def createPlugin(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self.plugin_tab, "Create New Plugin", "Name of Plugin:",
                                                         QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            dbnames = DBConnection.get_collection("plugin")
            coll = dbnames.list_collections()
            for i in coll:
                if text in i:
                    x= ErrorDialog(self.plugin_tab,"Plugin with that name already exists","Error Creating Plugin")
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
        pluginDB = DBConnection.get_collection("plugin")
        plgCllc = pluginDB[self.plugin_tab.DPVPluginName.text()]
        info = {"name": self.plugin_tab.DPVPluginName.text(), "desc": self.plugin_tab.DPVPluginDescription.toPlainText(),
                "poi": {"item":""}, "output": self.plugin_tab.DPVDefaultOutputField.text()}
        plg = Plugin.getName(self.plugin_tab.DPVPluginName.text())
        if not plg:
            plgCllc.insert(info, check_keys=False)
            x = ErrorDialog(self.plugin_tab,"Plugin Saved", "Save Plugin")
            x.exec_()
            self.pluginSignal.emit()
        else:
            x = ErrorDialog(self, "Plugin already exists", "Error Plugin")
            x.exec_()
            return

    def deletePlugin(self):
        if self.plugin != "":
            buttonReply = QtWidgets.QMessageBox.question(self.plugin_tab, 'PyQt5 message',
                                                         "Do you like to erase Plugin %s ?" % self.plugin,
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                         QtWidgets.QMessageBox.No)
            if buttonReply == QtWidgets.QMessageBox.Yes:
                projectDb = DBConnection.get_collection("plugin")
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
            x = ErrorDialog(self.plugin_tab,"Please select a plugin", "Error")
            x.exec_()

    def itemActivated(self):
        if self.plugin_tab.listWidget.count() != 0:
            pluginS = self.plugin_tab.listWidget.selectedItems()
            pluginName = [item.text().encode("ascii") for item in pluginS]
            if pluginName:
                try:
                    self.plugin = pluginName[0].decode()
                    cursor = Plugin.getName(self.plugin)
                    if cursor:
                        for pl in cursor:
                            self.plugin_tab.DPVPluginName.setText(pl["name"])
                            self.plugin_tab.DPVPluginDescription.setText(pl["desc"])
                            self.plugin_tab.DPVDefaultOutputField.setText(pl["output"])
                            for i in pl["poi"]["item"]:
                                lastText = self.plugin_tab.DVPPointOfInterest.toPlainText()
                                new = lastText + i["type"] + " " + i["name"] + "\n"
                                self.plugin_tab.DVPPointOfInterest.setText(new)
                except Exception as e:
                    x = pop.errorDialog(self.plugin_tab,str(e),"Error")
                    x.exec_()

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
