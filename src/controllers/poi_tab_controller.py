from PyQt5 import QtCore, QtGui, QtWidgets
import xmlschema
import pprint
from view import poi


class poi_tab_controller:

    def __init__(self, poi_tab):
        self.poi_tab = poi_tab

    def establish_connections(self):
        self.poi_tab.pois = self.dump_xml()
        self.poi_tab.POI.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.poi_tab.pois[0])))
        self.poi_tab.POI_2.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.poi_tab.pois[1])))
        self.poi_tab.POI_3.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.poi_tab.pois[2])))
        self.poi_tab.POI_4.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.poi_tab.pois[3])))
        self.poi_tab.POI_5.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.poi_tab.pois[4])))

    def dump_xml(self, dataset=None):
        # should require to get them from somewhere not straight xml.
        xmls = ['variable', 'string', 'dll', 'packet', 'function', 'struct']
        xml_d = []
        for f in xmls:
            print(self.poi_tab.my_schema.is_valid('resources/schemas/{}.xml'.format(f)))
            xml_d.append(self.poi_tab.my_schema.to_dict('resources/schemas/{}.xml'.format(f)))
        return xml_d

    def setup_poi_data(self, buttons, pois):
        '''fix this part to make it work better'''
        for item, data in zip(buttons, pois):
            print(item)
            item.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(data)))

    def display_editor_text(self, text):
        self.poi_tab.POI_content_area.setText(text)

    def create_pois(self, pois):
        buttns = []
        for poi in pois:
            pprint.pprint(poi)
            butn = QtWidgets.QPushButton(self.poi_tab.POI_list_view)
            butn.setFlat(True)
            butn.setObjectName(poi['name'])
            self.poi_tab.verticalLayout.addWidget(butn)
            self.poi_tab.POI_frame.addWidget(self.poi_tab.POI_list_view)
            butn.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(poi)))
            buttns.append(butn)
        return buttns
