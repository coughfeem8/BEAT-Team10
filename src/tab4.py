# Also known as tbe Point of Interest Tab
from PyQt5 import QtCore, QtGui, QtWidgets
import xmlschema
import xmltodict
import pprint
import src.ui.poi
import src.pop
from singleton import Singleton


class Tab4(src.ui.poi.Ui_POI_tab):
    def __init__(self, main, parent=None):
        super(Tab4, self).__init__(parent)
        self.setupUi(self)

        self.comboBox.currentIndexChanged.connect(lambda x: self.fillPOIs(plugin=self.comboBox.currentText()))
        self.comboBox_2.addItem("All")
        self.setPlugins()
        self.listWidget_2.itemSelectionChanged.connect(self.itemActivatedPlugin)
        self.comboBox_2.currentIndexChanged.connect(lambda x: self.filterPOIs(plugin=self.comboBox.currentText(),
                                                                              type=self.comboBox_2.currentText()))

        self.pushButton_11.clicked.connect(self.instantiateAddPOIWindow)



    def setPlugins(self):
        for pl in Singleton.getPlugins():
            with open('plugins/%s' %pl) as fd:
                doc = xmltodict.parse(fd.read())
                i = doc["plugin"]["name"]
                self.comboBox.addItem(i)


    def fillPOIs(self, plugin):
        for pl in Singleton.getPlugins():
            with open('plugins/%s' %pl) as fd:
                doc = xmltodict.parse(fd.read())
                if doc["plugin"]["name"] == plugin:
                    break
        types =[]
        for i in doc["plugin"]["point_of_interest"]:
            self.listWidget_2.addItem(i["name"])
            if i["type"] not in types:
                types.append(i["type"])
                self.comboBox_2.addItem(i["type"])

    def filterPOIs(self, plugin, type):
        self.listWidget_2.clear()
        for pl in Singleton.getPlugins():
            with open('plugins/%s' % pl) as fd:
                doc = xmltodict.parse(fd.read())
                if doc["plugin"]["name"] == plugin:
                    break

        for i in doc["plugin"]["point_of_interest"]:
            if type != "All":
                if i["type"] == type:
                    self.listWidget_2.addItem(i["name"])
            else:
                self.listWidget_2.addItem(i["name"])

    def itemActivatedPlugin(self):
        poiSelect = self.listWidget_2.selectedItems()
        poiName = [item.text().encode("ascii") for item in poiSelect]
        for pl in Singleton.getPlugins():
            with open('plugins/%s' % pl) as fd:
                doc = xmltodict.parse(fd.read())
                if doc["plugin"]["name"] == self.comboBox.currentText:
                    break
        if poiName:
            for i in doc["plugin"]["point_of_interest"]:
                if poiName[0].decode() == i["name"]:
                    self.textEdit.setText(i["name"]+" "+i["type"])
    def instantiateAddPOIWindow(self):
        pop = src.pop.addPOIDialog(self)
        comm = pop.exec_()

