from PyQt5 import QtCore, QtWidgets
from view import Tab1, Tab2, Tab3, Tab4, Tab5
from model.Singleton import Singleton
from controllers import ProjectTabController, AnalysisTabController, POITabController, PluginTabController, \
    DocumentationTabController


class UIMainWindow(QtWidgets.QMainWindow):
    """Creates the UI for the main window and controls its properties"""

    def setup_ui(self, main_window):
        """Sets up the ui for the main window and establishes the controllers and their connections for each tab"""
        self.main_window = main_window
        self.main_window.setObjectName("BEAT")
        self.main_window.resize(804, 615)
        self.main_window.setFixedSize(self.main_window.width(), self.main_window.height())

        self.main_window.setWindowTitle("BEAT")

        s = Singleton()
        s.set_project("BEAT")

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 794, 605))
        self.tabWidget.setObjectName("tabWidget")

        self.ProjectTab = Tab1.Tab1(self)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = Tab2.Tab2(self, self)
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = Tab3.Tab3(self, self)
        self.tabWidget.addTab(self.pluginTab, "")

        self.pointsOfInterestTab = Tab4.Tab4(self, self)
        self.tabWidget.addTab(self.pointsOfInterestTab, "")

        self.documentationTab = Tab5.Tab5(self, self)
        self.tabWidget.addTab(self.documentationTab, "")

        self.project_controller = ProjectTabController.ProjectTabController(self.ProjectTab)
        self.project_controller.establish_connections()
        self.project_controller.establish_calls()

        self.analysis_controller = AnalysisTabController.AnalysisTabController(self.analysisTab)
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

        self.project_controller.selected_project_changed.connect(
            lambda: self.analysis_controller.poi_comboBox_change("All"))
        self.project_controller.selected_project_changed.connect(lambda: self.set_project_name())
        self.project_controller.selected_project_changed.connect(lambda: self.analysisTab.terminal_output_textEdit.clear())
        self.project_controller.project_creation_started.connect(lambda: self.disable_tabs())
        self.project_controller.project_creation_finished.connect(lambda: self.enable_tabs())

        self.analysis_controller.dynamic_started.connect(lambda: self.set_running())
        self.analysis_controller.dynamic_stopped.connect(lambda: self.set_project_name())
        self.analysis_controller.dynamic_started.connect(lambda: self.disable_tabs())
        self.analysis_controller.dynamic_stopped.connect(lambda: self.enable_tabs())

        self.plugin_controller.plugin_signal.connect(self.analysis_controller.set_plugins)
        self.plugin_controller.plugin_signal.connect(self.poi_controller.set_plugins)
        self.plugin_controller.plugin_creation_started.connect(lambda: self.disable_tabs())
        self.plugin_controller.plugin_creation_finished.connect(lambda: self.enable_tabs())

        self.main_window.setCentralWidget(self.centralwidget)
        self.retranslate_ui()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        """Applies the translation qt call to the ui"""
        _translate = QtCore.QCoreApplication.translate

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProjectTab), _translate("MainWindow", "Project"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pluginTab), _translate("MainWindow", "Plugin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsOfInterestTab),
                                  _translate("MainWindow", "Points of Interest"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documentationTab),
                                  _translate("MainWindow", "Documentation"))

    def set_project_name(self):
        self.main_window.setWindowTitle("BEAT | " + Singleton.get_project())

    def set_running(self):
        self.main_window.setWindowTitle("BEAT | Running " + Singleton.get_project())

    def disable_tabs(self):
        """Disables any tab not currently in use when creating a new Project, Plugin, or running dynamic analysis"""
        for tab_index in range(self.tabWidget.count()):
            if tab_index != self.tabWidget.currentIndex():
                self.tabWidget.setTabEnabled(tab_index, False)
            self.tabWidget.setTabEnabled(4, True)

    def enable_tabs(self):
        """Enables all tabs once creation of a project or plugin finishes or dynamic analysis stops running"""
        for tab_index in range(self.tabWidget.count()):
            self.tabWidget.setTabEnabled(tab_index, True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
