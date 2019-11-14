from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from model import Plugin
import xmlschema


class PluginTabController:

    def __init__(self, plugin_tab):
        self.plugin_tab = plugin_tab

    def establish_connections(self):
        self.plugin_tab.pushButton_7.clicked.connect(self.create_plugin)
        self.plugin_tab.ButtonDPVPluginStructure.clicked.connect(self.browse_struct)
        self.plugin_tab.ButtonDPVBDataset.clicked.connect(self.browse_dataset)
        self.plugin_tab.listWidget.itemSelectionChanged.connect(self.item_activated)
        self.plugin_tab.lineEdit.textChanged.connect(
            lambda x: self.search_installed_plugins(self.plugin_tab.lineEdit.text()))

    def establish_calls(self):
        self.set_plugins()

    def set_plugins(self):
        for pl in Plugin.get_installed_plugins():
            self.plugin_tab.listWidget.addItem(pl)

    def browse_struct(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab, "Browse XML Schema", "",
                                                             "XML Schemas Files (*.xsd)", options=options)
        if file_name:
            self.plugin_tab.DPVPluginStructure.setText(file_name)

    def browse_dataset(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab, "Browse XML File", "",
                                                             "XML Files (*.xml)", options=options)
        if file_name:
            self.plugin_tab.DPVPluginDataSet.setText(file_name)

    def create_plugin(self):
        text, ok_pressed = QtWidgets.QInputDialog.getText(self.plugin_tab, "Create New Plugin", "Name of Plugin:",
                                                          QtWidgets.QLineEdit.Normal, "")
        print(text)

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
