# Also known as tbe Point of Interest Tab
import xmlschema
import view.poi


class Tab4(view.poi.Ui_POI_tab):
    def __init__(self, main, parent=None):
        super(Tab4, self).__init__(parent)
        self.setupUi(self)

        self.my_schema = xmlschema.XMLSchema('resources/schemas/network_plugin.xsd')
        self.pois = []
        # pois = self.create_pois(self.pois)
        self.pois_btns = [self.POI, self.POI_2, self.POI_3, self.POI_4, self.POI_5]
        # self.setup_poi_data(pois)
        #self.setup_poi_data(self.pois_btns, self.pois)