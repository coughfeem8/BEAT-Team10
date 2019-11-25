from view.pop.AddPOIDialog import AddPOIDialog
from model import Plugin
from PyQt5 import QtCore, QtWidgets, QtGui


class POITabController:

    def __init__(self, poi_tab):
        self.poi_tab = poi_tab
        self.poi_tab.comboBox_2.addItem("All")

    def establish_connections(self):
        self.poi_tab.pushButton_11.clicked.connect(self.add_poi)
        self.poi_tab.comboBox.currentIndexChanged.connect(lambda x: self.fill_poi(self.poi_tab.comboBox.currentText()))
        self.poi_tab.lineEdit_4.textChanged.connect(
            lambda x: self.search_installed_pois(self.poi_tab.lineEdit_4.text()))
        self.poi_tab.listWidget_2.itemSelectionChanged.connect(self.item_activated_event)
        self.poi_tab.pushButton_2.clicked.connect(self.delete_poi)

    def establish_calls(self):
        self.set_plugins()

    def set_plugins(self):
        self.poi_tab.comboBox.clear()
        for pl in Plugin.get_installed_plugins():
            self.poi_tab.comboBox.addItem(pl)

    def fill_poi(self, current):
        self.poi_tab.listWidget_2.clear()
        doc = Plugin.get_poi(current)
        if doc:
            types = []
            for i in doc["item"]:
                self.poi_tab.listWidget_2.addItem(i["name"])
                if i["type"] not in types:
                    types.append(i["type"])
                    self.poi_tab.comboBox_2.addItem(i["type"])

    def filter_poi(self, current, poi_type):
        self.poi_tab.listWidget_2.clear()
        doc = Plugin.get_poi(current)
        for i in doc["item"]:
            if poi_type != "All":
                if i["type"] == poi_type:
                    self.poi_tab.listWidget_2.addItem(i["name"])
            else:
                self.poi_tab.listWidget_2.addItem(i["name"])

    def add_poi(self):
        add_poi_pop_up = AddPOIDialog(self.poi_tab)
        pois = add_poi_pop_up.exec_()
        doc = Plugin.get_name(self.poi_tab.comboBox.currentText())
        if doc:
            for i in doc:
                new = i["poi"]["item"] + pois["item"]
                dict = {"item":new}
                Plugin.update_poi(dict, i["name"])
                self.filter_poi(self.poi_tab.comboBox.currentText(), self.poi_tab.comboBox_2.currentText())

    def delete_poi(self):
        poi = self.poi_tab.listWidget_2.selectedItems()
        poi_name = [item.text().encode("ascii") for item in poi]
        button_reply = QtWidgets.QMessageBox.question(self.poi_tab, 'PyQt5 message',
                                                      "Do you like to erase Poi %s ?" % poi_name[0].decode(),
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                      QtWidgets.QMessageBox.No)
        if button_reply == QtWidgets.QMessageBox.Yes and poi_name:
            Plugin.delete_poi(self.poi_tab.comboBox.currentText(),poi_name[0].decode())
            self.filter_poi(self.poi_tab.comboBox.currentText(), self.poi_tab.comboBox_2.currentText())

    def search_installed_pois(self, text):
        if len(text) is not 0:
            search_result = self.poi_tab.listWidget_2.findItems(text, QtCore.Qt.MatchContains)
            for item in range(self.poi_tab.listWidget_2.count()):
                self.poi_tab.listWidget_2.item(item).setHidden(True)
            for item in search_result:
                item.setHidden(False)
        else:
            for item in range(self.poi_tab.listWidget_2.count()):
                self.poi_tab.listWidget_2.item(item).setHidden(False)

    def item_activated_event(self):
        if self.poi_tab.listWidget_2.count() != 0:
            poi = self.poi_tab.listWidget_2.selectedItems()
            poi_name = [item.text().encode("ascii") for item in poi]
            if poi_name:
                cursor = Plugin.get_poi(self.poi_tab.comboBox.currentText())
                for i in cursor["item"]:
                    if i["name"] == poi_name[0].decode():
                        self.poi_tab.textEdit.setText(str(i))
                        break


