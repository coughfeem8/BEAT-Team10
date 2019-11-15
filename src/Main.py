from PyQt5 import QtCore, QtWidgets

from view import Tab1, Tab2, Tab3, Tab4, Tab5
from model.Singleton import Singleton
from model import Plugin
from controllers import ProjectTabController, AnalysisTabController, POITabController, PluginTabController , doc_tab_controller



class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("BEAT")
        MainWindow.resize(804, 615)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        MainWindow.setWindowTitle("BEAT")
        s = Singleton()
        s.set_project("BEAT")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 794, 605))
        self.tabWidget.setObjectName("tabWidget")

        self.ProjectTab = Tab1.Tab1(self, MainWindow)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = Tab2.Tab2(self, self)
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = Tab3.Tab3(self, self)
        self.tabWidget.addTab(self.pluginTab, "")

        self.pointsOfInterestTab = Tab4.Tab4(self, self)
        self.tabWidget.addTab(self.pointsOfInterestTab, "")

        self.documentationTab = Tab5.Tab5(self, self)
        self.tabWidget.addTab(self.documentationTab, "")

        self.project_controller = ProjectTabController.ProjectTabController(self.ProjectTab, MainWindow)
        self.project_controller.establish_connections()
        self.project_controller.establish_calls()

        self.analysis_controller = AnalysisTabController.AnalysisTabController(self.analysisTab, MainWindow)
        self.analysis_controller.establish_connections()
        self.analysis_controller.establish_calls()

        self.plugin_controller = PluginTabController.PluginTabController(self.pluginTab)
        self.plugin_controller.establish_connections()
        self.plugin_controller.establish_calls()

        self.poi_controller = POITabController.POITabController(self.pointsOfInterestTab)
        self.poi_controller.establish_connections()
        self.poi_controller.establish_calls()

        self.doc_controller = doc_tab_controller.doc_tab_controller(self.documentationTab)
        self.doc_controller.establish_connections()
        self.doc_controller.establish_calls()


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProjectTab), _translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pluginTab), _translate("MainWindow", "Plugin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsOfInterestTab),
                                  _translate("MainWindow", "Points of Interest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documentationTab),
                                  _translate("MainWindow", "Documentation"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
