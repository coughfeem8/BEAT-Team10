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
        self.poi_tab.comboBox.currentIndexChanged.connect(lambda x: self.fill_POIs(
            cplg=self.poi_tab.comboBox.currentText()))
        self.poi_tab.listWidget_2.itemSelectionChanged.connect(self.item_activated_plugin)
        self.poi_tab.comboBox_2.currentIndexChanged.connect(
            lambda x: self.filter_POIs(cplg=self.poi_tab.comboBox.currentText(),
                                       type=self.poi_tab.comboBox_2.currentText()))
        self.poi_tab.pushButton_11.clicked.connect(self.instantiate_add_poi_window)
        self.poi_tab.pushButton_2.clicked.connect(
            lambda x: self.delete_POI(poi=self.poi_tab.listWidget_2.selectedItems()))
        self.poi_tab.lineEdit_4.textChanged.connect(
            lambda x: self.search_installed_pois(self.poi_tab.lineEdit_4.text()))

    def establish_calls(self):
        self.set_plugins()

    def set_plugins(self):
        for pl in Plugin.get_installed_plugins():
            self.poi_tab.comboBox.addItem(pl)

    def fill_POIs(self, cplg):
        doc = Plugin.plugin_connection(cplg)
        types = []
        for i in doc["plugin"]["point_of_interest"]["item"]:
            self.poi_tab.listWidget_2.addItem(str(i["name"]))
            if i["type"] not in types:
                types.append(i["type"])
                self.poi_tab.comboBox_2.addItem(i["type"])

    def filter_POIs(self, cplg, type):
        self.poi_tab.listWidget_2.clear()
        doc = Plugin.plugin_connection(cplg)
        for i in doc["plugin"]["point_of_interest"]["item"]:
            if type != "All":
                print(i)
                if i["type"] == type:
                    self.poi_tab.listWidget_2.addItem(str(i["name"]))
            else:
                self.poi_tab.listWidget_2.addItem(str(i["name"]))

    def item_activated_plugin(self):
        poi_select = self.poi_tab.listWidget_2.selectedItems()
        poi_name = [item.text().encode("ascii") for item in poi_select]
        doc = Plugin.plugin_connection(self.poi_tab.comboBox.currentText)
        if poi_name:
            for i in doc["plugin"]["point_of_interest"]["item"]:
                if poi_name[0].decode() == i["name"]:
                    self.poi_tab.textEdit.setText(i["name"] + " " + i["type"])

    def instantiate_add_poi_window(self):
        pop = AddPOIDialog(self.poi_tab)
        text, out, type = pop.exec_()
        if text is "":
            return

        new_poi = {"name": text, "type": type, "pythonOutput": out}
        doc = Plugin.plugin_connection(self.poi_tab.comboBox.currentText)
        pl = Plugin.get_plugin_file(self.poi_tab.comboBox.currentText)
        old = doc["plugin"]["point_of_interest"]["item"]
        old.append(new_poi)
        doc["plugin"]["point_of_interest"] = old
        xml = dicttoxml.dicttoxml(doc, attr_type=False, root=False)
        dom = parseString(xml)
        wr = open('plugins/%s' % pl, 'w')
        wr.write(dom.toprettyxml())
        wr.close()
        self.filter_POIs(str(self.poi_tab.comboBox.currentText()), str(self.poi_tab.comboBox_2.currentText()))

    def delete_POI(self, poi):
        if not poi:
            return
        poi_name = [item.text().encode("ascii") for item in poi]
        doc = Plugin.plugin_connection(self.poi_tab.comboBox.currentText)
        old = doc["plugin"]["point_of_interest"]["item"]
        pl = Plugin.get_plugin_file(self.poi_tab.comboBox.currentText)
        name = poi_name[0].decode()
        i = 0
        for point in doc["plugin"]["point_of_interest"]["item"]:
            if name == point["name"]:
                del doc["plugin"]["point_of_interest"]["item"][i]
            i += 1
        doc["plugin"]["point_of_interest"] = old
        xml = dicttoxml.dicttoxml(doc, attr_type=False, root=False)
        dom = parseString(xml)
        wr = open('plugins/%s' % pl, 'w')
        wr.write(dom.toprettyxml())
        wr.close()
        self.poi_tab.textEdit.setText("")
        self.filter_POIs(str(self.poi_tab.comboBox.currentText()), str(self.poi_tab.comboBox_2.currentText()))

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
