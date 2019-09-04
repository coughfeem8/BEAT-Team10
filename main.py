
from PyQt5 import QtCore, QtGui, QtWidgets
import tab1, tab2, tab3, tab4, tab5


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 615)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setObjectName("tabWidget")

        self.ProjectTab = tab1.fillTab1()
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = tab2.fillTab2()
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = QtWidgets.QWidget()
        self.pluginTab.setObjectName("pluginTab")
        self.tabWidget.addTab(self.pluginTab, "")
        self.pointsOfInterestTab = QtWidgets.QWidget()
        self.pointsOfInterestTab.setObjectName("pointsOfInterestTab")
        self.tabWidget.addTab(self.pointsOfInterestTab, "")
        self.documentationTab = QtWidgets.QWidget()
        self.documentationTab.setObjectName("documentationTab")
        self.tabWidget.addTab(self.documentationTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

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