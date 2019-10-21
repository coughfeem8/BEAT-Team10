# Also known as tbe Point of Interest Tab
from PyQt5 import QtCore, QtGui, QtWidgets
import xmlschema
import pprint
import view.poi


class Tab4(view.poi.Ui_POI_tab):
    def __init__(self, main, parent=None):
        super(Tab4, self).__init__(parent)
        self.setupUi(self)

        self.my_schema = xmlschema.XMLSchema('resources/schemas/network_plugin.xsd')
        self.pois = []
        self.pois = self.dump_xml()
        # pois = self.create_pois(self.pois)
        self.pois_btns = [self.POI, self.POI_2, self.POI_3, self.POI_4, self.POI_5]
        # self.setup_poi_data(pois)
        #self.setup_poi_data(self.pois_btns, self.pois)
        self.POI.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.pois[0])))
        self.POI_2.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.pois[1])))
        self.POI_3.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.pois[2])))
        self.POI_4.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.pois[3])))
        self.POI_5.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(self.pois[4])))


    def dump_xml(self, dataset=None):
        # should require to get them from somewhere not straight xml.
        xmls = ['variable', 'string', 'dll', 'packet', 'function', 'struct']
        xml_d = []
        for f in xmls:
            print(self.my_schema.is_valid('resources/schemas/{}.xml'.format(f)))
            xml_d.append(self.my_schema.to_dict('resources/schemas/{}.xml'.format(f)))
        return xml_d

    def setup_poi_data(self, buttons, pois):
        '''fix this part to make it work better'''
        for item, data in zip(buttons,pois):
            print(item)
            item.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(data)))


    def display_editor_text(self, text):
        self.POI_content_area.setText(text)


    def create_pois(self, pois):
        buttns = []
        for poi in pois:
            pprint.pprint(poi)
            butn = QtWidgets.QPushButton(self.POI_list_view)
            butn.setFlat(True)
            butn.setObjectName(poi['name'])
            self.verticalLayout.addWidget(butn)
            self.POI_frame.addWidget(self.POI_list_view)
            butn.clicked.connect(lambda x: self.display_editor_text(pprint.pformat(poi)))
            buttns.append(butn)
        return buttns
