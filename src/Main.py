from PyQt5 import QtCore, QtWidgets
from view import Tab1, Tab2, Tab3, Tab4, Tab5
from model.Singleton import Singleton
from controllers import ProjectTabController, AnalysisTabController, POITabController, PluginTabController, \
    DocumentationTabController


class UIMainWindow(QtWidgets.QMainWindow):
    def setup_ui(self, main_window):
        main_window.setObjectName("BEAT")
        main_window.resize(804, 615)
        main_window.setFixedSize(main_window.width(), main_window.height())

        main_window.setWindowTitle("BEAT")
        s = Singleton()
        s.set_project("BEAT")

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 794, 605))
        self.tabWidget.setObjectName("tabWidget")

        self.ProjectTab = Tab1.Tab1(self, main_window)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = Tab2.Tab2(self, self)
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = Tab3.Tab3(self, self)
        self.tabWidget.addTab(self.pluginTab, "")

        self.pointsOfInterestTab = Tab4.Tab4(self, self)
        self.tabWidget.addTab(self.pointsOfInterestTab, "")

        self.documentationTab = Tab5.Tab5(self, self)
        self.tabWidget.addTab(self.documentationTab, "")

        self.project_controller = ProjectTabController.ProjectTabController(self.ProjectTab, main_window)
        self.project_controller.establish_connections()
        self.project_controller.establish_calls()

        self.analysis_controller = AnalysisTabController.AnalysisTabController(self.analysisTab, main_window)
        self.analysis_controller.establish_connections()
        self.analysis_controller.establish_calls()

        self.plugin_controller = PluginTabController.PluginTabController(self.pluginTab)
        self.plugin_controller.establish_connections()
        self.plugin_controller.establish_calls()

        self.poi_controller = POITabController.POITabController(self.pointsOfInterestTab)
        self.poi_controller.establish_connections()
        self.poi_controller.establish_calls()

        self.doc_controller = DocumentationTabController.DocumentationTabController(self.documentationTab)
        self.doc_controller.establish_connections()
        self.doc_controller.establish_calls()

        self.plugin_controller.pluginSignal.connect(self.analysis_controller.set_plugins)
        self.plugin_controller.pluginSignal.connect(self.poi_controller.set_plugins)
        self.project_controller.projectSignal.connect(lambda:self.analysis_controller.poi_comboBox_change("All"))

        main_window.setCentralWidget(self.centralwidget)
        self.retranslate_ui(main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
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
    ui = UIMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
