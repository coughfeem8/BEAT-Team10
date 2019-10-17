from PyQt5 import QtCore, QtGui, QtWidgets
import pop
import base64
from singleton import Singleton
import pymongo
import analysis

class Tab2(QtWidgets.QWidget):
    def __init__(self, parent, main):
        QtWidgets.QWidget.__init__(self, parent)

        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.plugin_label = QtWidgets.QLabel(self)
        self.plugin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.plugin_label.setObjectName("plugin_label")
        self.gridLayout_2.addWidget(self.plugin_label, 0, 0, 1, 1)

        self.plugin_comboBox = QtWidgets.QComboBox(self)
        self.plugin_comboBox.setMaxVisibleItems(10)
        self.plugin_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.plugin_comboBox.setObjectName("plugin_comboBox")
        self.plugin_comboBox.addItem("")
        self.plugin_comboBox.addItem("")
        self.plugin_comboBox.addItem("")
        self.gridLayout_2.addWidget(self.plugin_comboBox, 0, 1, 1, 1)

        self.static_anal_label = QtWidgets.QLabel(self)
        self.static_anal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.static_anal_label.setObjectName("static_anal_label")
        self.gridLayout_2.addWidget(self.static_anal_label, 1, 0, 1, 1)
        self.static_run_button = QtWidgets.QPushButton(self)
        self.static_run_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.static_run_button.setObjectName("static_run_button")
        self.gridLayout_2.addWidget(self.static_run_button, 1, 1, 1, 1)

        self.dynamic_anal_label = QtWidgets.QLabel(self)
        self.dynamic_anal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dynamic_anal_label.setObjectName("dynamic_anal_label")
        self.gridLayout_2.addWidget(self.dynamic_anal_label, 1, 2, 1, 1)
        self.dynamic_run_button = QtWidgets.QPushButton(self)
        self.dynamic_run_button.setObjectName("dynamic_run_button")
        self.gridLayout_2.addWidget(self.dynamic_run_button, 1, 3, 2, 1)
        self.dynamic_stop_button = QtWidgets.QPushButton(self)
        self.dynamic_stop_button.setObjectName("dynamic_stop_button")
        self.gridLayout_2.addWidget(self.dynamic_stop_button, 1, 4, 2, 1)
        self.dynamic_run_button.clicked.connect(self.breakpoint_check)

        self.poi_comboBox = QtWidgets.QComboBox(self)
        self.poi_comboBox.setObjectName("poi_comboBox")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.gridLayout_2.addWidget(self.poi_comboBox, 2, 1, 2, 1)

        self.poi_label = QtWidgets.QLabel(self)
        self.poi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.poi_label.setObjectName("poi_label")
        self.gridLayout_2.addWidget(self.poi_label, 3, 0, 1, 1)

        self.comment_PushButton = QtWidgets.QPushButton(self)
        self.comment_PushButton.setObjectName("comment_PushButton")
        self.gridLayout_2.addWidget(self.comment_PushButton, 3, 2, 1, 1)
        self.comment_PushButton.clicked.connect(self.open_comment)

        self.analysis_PushButton = QtWidgets.QPushButton(self)
        self.analysis_PushButton.setObjectName("analysis_PushButton")
        self.gridLayout_2.addWidget(self.analysis_PushButton, 3, 3, 1, 1)
        self.analysis_PushButton.clicked.connect(self.open_analysis)

        self.output_PushButton = QtWidgets.QPushButton(self)
        self.output_PushButton.setObjectName("output_PushButton")
        self.gridLayout_2.addWidget(self.output_PushButton, 3, 4, 1, 1)
        self.output_PushButton.clicked.connect(self.open_output)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.poi_title_label = QtWidgets.QLabel(self)
        self.poi_title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.poi_title_label.setAutoFillBackground(False)
        self.poi_title_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(0, 170, 255);")
        self.poi_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.poi_title_label.setObjectName("poi_title_label")
        self.gridLayout_6.addWidget(self.poi_title_label, 0, 1, 1, 1)

        self.search_bar_lineEdit = QtWidgets.QLineEdit(self)
        self.search_bar_lineEdit.setFrame(True)
        self.search_bar_lineEdit.setObjectName("search_bar_lineEdit")
        self.gridLayout_6.addWidget(self.search_bar_lineEdit, 1, 1, 1, 1)

        self.poi_listWidget = QtWidgets.QListWidget(self)
        self.poi_listWidget.setObjectName("listView")
        self.gridLayout_6.addWidget(self.poi_listWidget, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 4, 0, 2, 2)

        self.scrollArea_2 = QtWidgets.QScrollArea(self)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 505, 418))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName("gridLayout")

        self.terminal_window_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.terminal_window_lineEdit.setObjectName("terminal_window_lineEdit")
        self.gridLayout.addWidget(self.terminal_window_lineEdit, 3, 0, 1, 2)

        self.poi_content_area_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.poi_content_area_textEdit.setObjectName("poi_content_area_textEdit")
        self.gridLayout.addWidget(self.poi_content_area_textEdit, 0, 0, 2, 1)

        self.terminal_output_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.terminal_output_textEdit.setObjectName("terminal_output_textEdit")
        self.gridLayout.addWidget(self.terminal_output_textEdit, 2, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea_2, 5, 2, 1, 3)

        self.detailed_poi_view_label = QtWidgets.QLabel(self)
        self.detailed_poi_view_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                                   "background-color: rgb(0, 170, 255);")
        self.detailed_poi_view_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detailed_poi_view_label.setObjectName("detailed_poi_view_label")
        self.gridLayout_2.addWidget(self.detailed_poi_view_label, 4, 2, 1, 3)

        _translate = QtCore.QCoreApplication.translate

        self.plugin_label.setText(_translate("MainWindow", "Plugin"))

        self.plugin_comboBox.setItemText(0, _translate("MainWindow", "Network Plugin"))
        self.plugin_comboBox.setItemText(1, _translate("MainWindow", "Plugin A"))
        self.plugin_comboBox.setItemText(2, _translate("MainWindow", "Plugin B"))

        self.static_anal_label.setText(_translate("MainWindow", "Static Analysis"))
        self.static_run_button.setText(_translate("MainWindow", "Run"))
        self.dynamic_anal_label.setText(_translate("MainWindow", "Dynamic Analysis"))
        self.dynamic_run_button.setText(_translate("MainWindow", "Run"))
        self.dynamic_stop_button.setText(_translate("MainWindow", "Stop"))

        self.poi_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.poi_comboBox.setItemText(1, _translate("MainWindow", "Variables"))
        self.poi_comboBox.setItemText(2, _translate("MainWindow", "Strings"))
        self.poi_comboBox.setItemText(3, _translate("MainWindow", "DLLs"))
        self.poi_comboBox.setItemText(4, _translate("MainWindow", "Functions"))
        self.poi_comboBox.setItemText(5, _translate("MainWindow", "Packets"))
        self.poi_comboBox.setItemText(6, _translate("MainWindow", "Structs"))
        self.poi_comboBox.currentIndexChanged.connect(lambda x: self.poi_comboBox_change(text=self.poi_comboBox.currentText()))

        self.poi_label.setText(_translate("MainWindow", "Point of Interest"))

        self.comment_PushButton.setText(_translate("MainWindow", "Comment"))
        self.analysis_PushButton.setText(_translate("MainWindow", "Analysis"))
        self.output_PushButton.setText(_translate("MainWindow", "Output"))

        self.poi_title_label.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Point of "
                                                "Interest View</span></p></body></html>"))
        self.detailed_poi_view_label.setText(_translate("MainWindow",
                                                        "<html><head/><body><p><span style=\" "
                                                        "font-weight:600;\">Detailed Point of Interst "
                                                        "View</span></p></body></html>"))

    def open_comment(self):
        popUp = pop.commentDialog(self)
        text = popUp.exec_()
        print(text)

    def open_analysis(self):
        popUp = pop.analysisResultDialog(self)
        text = popUp.exec_()
        print(text)

    def open_output(self):
        popUp = pop.outputFieldDialog(self)
        text = popUp.exec_()
        print(text)

    def set_item(self, text, type):
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(QtCore.Qt.Checked)
        item.setToolTip(type)
        return item

    def breakpoint_check(self):
        for i in range(self.poi_listWidget.count()):
            item = self.poi_listWidget.item(i)
            print(f"{i} {item.text()} {item.checkState()}")

    def detailed_poi(self, item):
        s = Singleton.getProject()
        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]

        lastText = self.poi_content_area_textEdit.toPlainText()

        if item.toolTip() == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find_one({"signature": item.text()})
        elif item.toolTip() == "Variables":
            projInfo = projectDb["variables"]
            var = item.text().split()
            cursor = projInfo.find_one({"name": var[1]})
        elif item.toolTip() == "Imports":
            projInfo = projectDb["imports"]
            text = item.text().split()
            cursor = projInfo.find_one({"name": text[0]})
        elif item.toolTip() == "Strings":
            projInfo = projectDb["string"]
            cursor = projInfo.find_one({"string": item.text()})
        elif item.toolTip() == "Structs":
            projInfo = projectDb["structures"]
            text = item.text().split()
            cursor = projInfo.find_one({"from": int(text[2], 0)})
        del cursor['_id']
        y = str(cursor)
        lastText = lastText.replace("\n" + y, ' ')
        self.poi_content_area_textEdit.setPlainText(y)

    def poi_comboBox_change(self, text):
        s = Singleton.getProject()
        if s == "BEAT":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        self.poi_listWidget.clear()

        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]

        if text == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["signature"], "Functions")
                self.poi_listWidget.addItem(item)
        elif text == "Variables":
            projInfo = projectDb['variables']
            coursor = projInfo.find()
            for db in coursor:
                item = self.set_item("%s %s" % (db["type"], db["name"]), "Variables")
                self.poi_listWidget.addItem(item)
        elif text == "DLLs":
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["name"] + " " + db["type"], "Imports")
                self.poi_listWidget.addItem(item)
        elif text == "Structs":
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:

                insert_send = {"address": hex(db["from"]), "opcode": db["opcode"],
                               "calling_function": db["fcn_name"]}
                item = self.set_item("send " + insert_send["calling_function"] + " " + insert_send["address"],
                                          "Structs")
                self.poi_listWidget.addItem(item)
        elif text == "Strings":
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.poi_listWidget.addItem(item)

        elif text == "All":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["signature"], "Functions")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["variables"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item("%s %s" % (db["type"], db["name"]), "Variables")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:
                insert_send = {"address": hex(db["from"]), "opcode": db["opcode"],
                               "calling_function": db["fcn_name"]}
                item = self.set_item("send " + insert_send["calling_function"] + " " + insert_send["address"],
                                    "Structs")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                text = base64.b64decode(db["string"])
                item = self.set_item(text.decode(), "Strings")
                self.poi_listWidget.addItem(item)
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                item = self.set_item(db["name"] + " " + db["type"], "Imports")
                self.poi_listWidget.addItem(item)
