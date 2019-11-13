import xmlschema
import xmltodict
import dicttoxml
import view.poi
from view import pop
from model import plugin
from PyQt5 import QtCore, QtWidgets, QtGui
from xml.dom.minidom import parseString


class poi_tab_controller:

    def __init__(self, poi_tab):
        self.poi_tab = poi_tab
        self.poi_tab.comboBox_2.addItem("All")

    def establish_connections(self):
        self.poi_tab.pushButton_11.clicked.connect(self.addPOI)
        self.poi_tab.comboBox.currentIndexChanged.connect(lambda x: self.fillPOI(self.poi_tab.comboBox.currentText()))

    def establish_calls(self):
        self.setPlugins()

    def setPlugins(self):
        self.poi_tab.comboBox.clear()
        for pl in plugin.getInstalled():
            self.poi_tab.comboBox.addItem(pl)

    def fillPOI(self, current):
        doc = plugin.getPOI(current)
        types = []
        for i in doc["item"]:
            self.poi_tab.listWidget_2.addItem(i["name"])
            if i["type"] not in types:
                types.append(i["type"])
                self.poi_tab.comboBox_2.addItem(i["type"])

    def filterPOI(self, current, type):
        self.poi_tab.listWidget_2.clear()
        doc = plugin.getPOI(current)
        for i in doc["item"]:
            if type != "All":
                if i["type"] == type:
                    self.poi_tab.listWidget_2.addItem(i["name"])
            else:
                self.poi_tab.listWidget_2.addItem(i["name"])

    def addPOI(self):
        popAdd = pop.addPOIDialog(self.poi_tab)
        pois = popAdd.exec_()
        doc = plugin.getName(self.poi_tab.comboBox.currentText())
        if doc:
            for i in doc:
                tmp = i["poi"]
                tmp.update(pois)
                print(i["poi"])
                #plugin.updatePOI(i["poi"], i["name"])
                self.fillPOI(self.poi_tab.comboBox.currentText())

