import dicttoxml
from view.pop.AddPOIDialog import AddPOIDialog
from model import Plugin
from xml.dom.minidom import parseString
from PyQt5 import QtCore, QtWidgets, QtGui


class POITabController:

    def __init__(self, poi_tab):
        self.poi_tab = poi_tab
        self.poi_tab.comboBox_2.addItem("All")

    def establish_connections(self):
        self.poi_tab.pushButton_11.clicked.connect(self.addPOI)
        self.poi_tab.comboBox.currentIndexChanged.connect(lambda x: self.fillPOI(self.poi_tab.comboBox.currentText()))
        self.poi_tab.lineEdit_4.textChanged.connect(
            lambda x: self.search_installed_pois(self.poi_tab.lineEdit_4.text()))

    def establish_calls(self):
        self.set_plugins()


    def set_plugins(self):
        self.poi_tab.comboBox.clear()
        for pl in Plugin.get_installed_plugins():
            self.poi_tab.comboBox.addItem(pl)

    def fillPOI(self, current):
        doc = Plugin.getPOI(current)
        types = []
        for i in doc["item"]:
            self.poi_tab.listWidget_2.addItem(i["name"])
            if i["type"] not in types:
                types.append(i["type"])
                self.poi_tab.comboBox_2.addItem(i["type"])

    def filterPOI(self, current, type):
        self.poi_tab.listWidget_2.clear()
        doc = Plugin.getPOI(current)
        for i in doc["item"]:
            if type != "All":
                if i["type"] == type:
                    self.poi_tab.listWidget_2.addItem(i["name"])
            else:
                self.poi_tab.listWidget_2.addItem(i["name"])

    def addPOI(self):
        popAdd = AddPOIDialog(self.poi_tab)
        pois = popAdd.exec_()
        doc = Plugin.getName(self.poi_tab.comboBox.currentText())
        if doc:
            for i in doc:
                tmp = i["poi"]
                tmp.update(pois)
                print(i["poi"])
                #plugin.updatePOI(i["poi"], i["name"])
                self.fillPOI(self.poi_tab.comboBox.currentText())

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
