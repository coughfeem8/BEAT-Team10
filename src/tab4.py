# Also known as tbe Point of Interest Tab
from PyQt5 import QtCore, QtGui, QtWidgets
import xmlschema
import xmltodict
import pprint
import ui.poi
from singleton import Singleton


class Tab4(ui.poi.Ui_POI_tab):
    def __init__(self, main, parent=None):
        super(Tab4, self).__init__(parent)
        self.setupUi(self)

        self.comboBox.currentIndexChanged.connect(lambda x: self.fillPOIs(plugin=self.comboBox.currentText()))
        self.comboBox_2.addItem("All")
        self.setPlugins()
        self.listWidget_2.itemSelectionChanged.connect(self.itemActivated_event)


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
        for i in doc["plugin"]["point_of_interest"]:
            self.listWidget_2.addItem(i["name"])

    def filterPOIs(self, plugin, type):
        for pl in Singleton.getPlugins():
            with open('plugins/%s' % pl) as fd:
                doc = xmltodict.parse(fd.read())
                if doc["plugin"]["name"] == plugin:
                    break
        for i in doc["plugin"]["point_of_interest"]:
            if i["type"] == type:
                self.listWidget_2.addItem(i["name"])

    def itemActivated_event(self):
        with open('plugins/netPOI.xml') as fd:
            doc = xmltodict.parse(fd.read())
        poiSelect = self.listWidget_2.selectedItems()
        poiName = [item.text().encode("ascii") for item in poiSelect]
        if poiName:
            for i in doc["plugin"]["point_of_interest"]:
                if poiName[0].decode() == i["name"]:
                    self.textEdit.setText(i["name"]+" "+i["type"])