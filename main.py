import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
import tab1

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'BEAT: Beahavioral Extraction Tool'
        self.left = 200
        self.top = 500
        self.width = 800
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(800, 800)

        self.tabs.addTab(self.tab1, "Project")
        self.tabs.addTab(self.tab2, "Analysis")
        self.tabs.addTab(self.tab3, "Plugin Management")
        self.tabs.addTab(self.tab4, "Points of Interest")
        self.tabs.addTab(self.tab5, "Documentation")


        self.tab1.setLayout(tab1.fillTab1(self.tab1, parent))

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
