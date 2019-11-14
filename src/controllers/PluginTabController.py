from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from model import Plugin, DBConnection
from view.pop import ErrorDialog
import xmlschema


class PluginTabController:

    plugin_signal = QtCore.pyqtSignal()

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab
        self.plugin = ""

    def establish_connections(self):
        self.plugin_tab.pushButton_7.clicked.connect(self.create_plugin)
        self.plugin_tab.listWidget.itemSelectionChanged.connect(self.item_activated)
        self.plugin_tab.ButtonSavePlugin.clicked.connect(self.save_plugin)
        self.plugin_tab.ButtonDeletePlugin.clicked.connect(self.delete_plugin)

    def establish_calls(self):
        self.set_plugins()

    def set_plugins(self):
        self.plugin_tab.listWidget.clear()
        for pl in Plugin.get_installed_plugins():
            self.plugin_tab.listWidget.addItem(pl)

    def create_plugin(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self.plugin_tab, "Create New Plugin", "Name of Plugin:",
                                                          QtWidgets.QLineEdit.Normal, "")
        if ok_pressed and text != "":
            coll = DBConnection.list_collections("plugin")
            for i in coll:
                if text in i:
                    x = ErrorDialog(self.plugin_tab,"Plugin with that name already exists","Error Creating Plugin")
                    x.e

    def delete_plugin(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Project")
        button_reply = QtWidgets.QMessageBox.question(self.plugin_tab, 'PyQt5 message',
                                                      "Are you sure to delete Plugin ?",
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes:
            self.plugin_tab.DPVPluginStructure.setText("")
            self.plugin_tab.DPVPluginDataSet.setText("")
            self.plugin_tab.DPVPluginDescription.setText("")
            self.plugin_tab.DPVPluginName.setText("")
            self.plugin_tab.DVPPointOfInterest.setText("")

    def item_activated(self):
        plg_select = self.plugin_tab.listWidget.selectedItems()
        plg_name = [item.text().encode("ascii") for item in plg_select]
        doc = Plugin.plugin_connection(plg_name)
        pl = Plugin.get_plugin_file(plg_name)
        xms = pl.split('.')[0] + '.xsd'
        schema = xmlschema.XMLSchema('plugins/%s' % xms)
        if plg_name:
            self.plugin_tab.DPVPluginName.setText(doc["plugin"]["name"])
            self.plugin_tab.DPVPluginDescription.setText(doc["plugin"]["description"])
            self.plugin_tab.DPVPluginDataSet.setText('plugins/%s' % pl)
            self.plugin_tab.DPVPluginStructure.setText('plugins/%s' % xms)
            for i in doc["plugin"]["point_of_interest"]["item"]:
                last_text = self.plugin_tab.DVPPointOfInterest.toPlainText()
                new = last_text + i["type"] + " " + i["name"] + "\n"
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
