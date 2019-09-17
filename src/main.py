
from PyQt5 import QtCore, QtGui, QtWidgets
import tab1, tab2, tab3, tab4, tab5


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        self.activeProj = "BEAT"
        MainWindow.setObjectName(self.activeProj)
        MainWindow.resize(804, 615)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        MainWindow.setWindowTitle(self.activeProj)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 791, 605))
        self.tabWidget.setObjectName("tabWidget")


        self.ProjectTab = tab1.Tab1(self, self)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.analysisTab = tab2.Tab2(self, self)
        self.tabWidget.addTab(self.analysisTab, "")

        self.pluginTab = tab3.Tab3(self, self)
        self.tabWidget.addTab(self.pluginTab, "")

        self.pointsOfInterestTab = tab4.fillTab4()
        self.tabWidget.addTab(self.pointsOfInterestTab, "")

        self.documentationTab = tab5.Tab5(self, self)
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
