from PyQt5 import QtCore, QtGui, QtWidgets
import src.tab1, src.tab2, src.tab3, src.tab4,src.tab5
from singleton import Singleton
from os import walk


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("BEAT")
        MainWindow.resize(804, 615)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        MainWindow.setWindowTitle("BEAT")
        s = Singleton()
        s.setProject("BEAT")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 794, 605))
        self.tabWidget.setObjectName("tabWidget")

        f = []
        for (dirpath, dirnames, filenames) in walk('./plugins'):
            for name in filenames:
                if name.endswith('.xml'):
                    f.append(name)
            break
        Singleton.setPlugins(f)

        self.ProjectTab = src.tab1.Tab1(self, MainWindow)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = src.tab2.Tab2(self, self)
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = src.tab3.Tab3(self, self)
        self.tabWidget.addTab(self.pluginTab, "")

        self.pointsOfInterestTab = src.tab4.Tab4(self,self)
        self.tabWidget.addTab(self.pointsOfInterestTab, "")

        self.documentationTab = src.tab5.Tab5(self, self)
        self.tabWidget.addTab(self.documentationTab, "")


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProjectTab), _translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pluginTab), _translate("MainWindow", "Plugin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsOfInterestTab), _translate("MainWindow", "Points of Interest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documentationTab), _translate("MainWindow", "Documentation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
