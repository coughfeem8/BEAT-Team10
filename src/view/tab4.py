# Also known as tbe Point of Interest Tab
import xmlschema
import view.poi


class Tab4(view.poi.Ui_POI_tab):
    def __init__(self, main, parent=None):
        super(Tab4, self).__init__(parent)
        self.setupUi(self)
