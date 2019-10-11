from PyQt5 import QtCore, QtGui, QtWidgets
import pop
import r2pipe
import base64
from singleton import Singleton
import pymongo


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
        self.static_run_button.clicked.connect(self.staticAna)

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
        self.comment_PushButton.clicked.connect(self.openComment)

        self.analysis_PushButton = QtWidgets.QPushButton(self)
        self.analysis_PushButton.setObjectName("analysis_PushButton")
        self.gridLayout_2.addWidget(self.analysis_PushButton, 3, 3, 1, 1)
        self.analysis_PushButton.clicked.connect(self.openAnalysis)

        self.output_PushButton = QtWidgets.QPushButton(self)
        self.output_PushButton.setObjectName("output_PushButton")
        self.gridLayout_2.addWidget(self.output_PushButton, 3, 4, 1, 1)
        self.output_PushButton.clicked.connect(self.openOutput)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.search_bar_lineEdit = QtWidgets.QLineEdit(self)
        self.search_bar_lineEdit.setFrame(True)
        self.search_bar_lineEdit.setObjectName("search_bar_lineEdit")
        self.horizontalLayout.addWidget(self.search_bar_lineEdit)

        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 332, 383))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.addWidget(self.scrollArea, 2, 1, 1, 1)

        self.poi_title_label = QtWidgets.QLabel(self)
        self.poi_title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.poi_title_label.setAutoFillBackground(False)
        self.poi_title_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(0, 170, 255);")
        self.poi_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.poi_title_label.setObjectName("poi_title_label")
        self.gridLayout_6.addWidget(self.poi_title_label, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 4, 0, 2, 2)
        self.scrollArea_2 = QtWidgets.QScrollArea(self)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 505, 418))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)

        self.gridLayout.setObjectName("gridLayout")
        self.poi_content_area_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.poi_content_area_textEdit.setObjectName("poi_content_area_textEdit")
        self.gridLayout.addWidget(self.poi_content_area_textEdit, 0, 0, 2, 1)

        self.terminal_window_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.terminal_window_lineEdit.setObjectName("terminal_window_lineEdit")
        self.gridLayout.addWidget(self.terminal_window_lineEdit, 2, 0, 1, 2)

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
        self.poi_comboBox.currentIndexChanged.connect(lambda x: self.poiComBxChng(text=self.poi_comboBox.currentText()))

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



    def openComment(self):
        popUp = pop.commentDialog(self)
        text = popUp.exec_()
        print(text)

    def openAnalysis(self):
        popUp = pop.analysisResultDialog(self)
        text = popUp.exec_()
        print(text)

    def openOutput(self):
        popUp = pop.outputFieldDialog(self)
        text = popUp.exec_()
        print(text)

    def staticAna(self):
        s = Singleton.getProject()
        if (s=="BEAT"):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]
        projInfo = projectDb["projectInfo"]
        cursor = projInfo.find()
        for db in cursor:
            binaryFile = db['BnyFilePath']

        for i in reversed(range(self.gridLayout_4.count())):
            self.gridLayout_4.itemAt(i).widget().setParent(None)
        try:
            rlocal = r2pipe.open(binaryFile)
            rlocal.cmd("aaa")
            i = 0

            # Gets all functions is JSON format
            functions = rlocal.cmdj("aflj")
            if projectDb["functions"]:
                projectDb.drop_collection("functions")
            fnctDB = projectDb["functions"]
            for fc in functions:
                checkBoxRecv =  QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText(fc["signature"])
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
                insert_info = {'offset': fc["offset"],'name':fc["name"],'size':fc["size"],'signature':fc["signature"]}
                fnctDB.insert_one(insert_info)

            # Gets all variables in JSON format
            '''
            varDB = projectDb["variable"]
            var = rlocal.cmdj("afvj")
            for variable in var:
                #var = variable.split()
                #if var[var.index("=") + 1] == ":":
                #    var_value = None
                #    var.insert(var.index('=') + 1, var_value)
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText("%s %s" % (variable[0], variable[1]))
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
                varDB.insert_one(variable)
            '''
            # Gets all structs in JSON format
            if projectDb["structures"]:
                projectDb.drop_collection("structures")
            strucDB = projectDb["structures"]
            all_recvs = rlocal.cmdj("axtj sym.imp.recv")
            all_sends = rlocal.cmdj("axtj sym.imp.send")

            for rec in all_recvs:
                insert_recv = {"address" : hex(rec["from"]), "opcode" : rec["opcode"], "calling_function" : rec["fcn_name"]}
                checkBoxRecv =  QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText("recv "+insert_recv["calling_function"] +" "+ insert_recv["address"])
                checkBoxRecv.stateChanged.connect(lambda: self.checkState(checkBoxRecv.text()))
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
                strucDB.insert_one(rec)

            for send in all_sends:
                insert_send = {"address" : hex(send["from"]), "opcode" : send["opcode"], "calling_function" : send["fcn_name"]}
                checkBoxSend =  QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxSend.setText("send "+insert_send["calling_function"] +" "+ insert_send["address"])
                checkBoxSend.stateChanged.connect(self.checkState)
                self.gridLayout_4.addWidget(checkBoxSend, i, 0, 1, 1)
                i += 1
                strucDB.insert_one(send)


            # Gets all strings in JSON format
            strings = rlocal.cmdj("izzj")
            if projectDb["string"]:
                projectDb.drop_collection("string")
            strDB = projectDb["string"]
            for string in strings:
                if(string["section"] == '.rodata'):
                    checkBoxSend = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                    checkBoxSend.setText((base64.b64decode(string["string"])).decode())
                    self.gridLayout_4.addWidget(checkBoxSend, i, 0, 1, 1)
                    i += 1
                    strDB.insert_one(string)

            # Gets all imports in JSON format
            imports = rlocal.cmdj("iij")
            if projectDb["imports"]:
                projectDb.drop_collection("imports")
            impDB = projectDb["imports"]
            for dl in imports:
                checkBoxSend = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxSend.setText(dl["name"]+" "+dl["type"])
                self.gridLayout_4.addWidget(checkBoxSend, i, 0, 1, 1)
                i += 1
                impDB.insert_one(dl)


        except Exception as e:
            print("Error " + str(e))
        QtWidgets.QApplication.restoreOverrideCursor()

    def checkState(self, state):
        print(state)

    def poiComBxChng(self, text):
        s = Singleton.getProject()
        if s == "BEAT":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Run Static Analysis")
            msg.setText("Please select a project")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        for i in reversed(range(self.gridLayout_4.count())):
            self.gridLayout_4.itemAt(i).widget().setParent(None)

        mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
        projectDb = mongoClient[s]
        i =0

        if text == "Functions":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText(db["signature"])
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
        elif text == "DLL":
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText(db["name"]+" "+db["type"])
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1

        elif text == "Structs":
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText("recv "+db["fcn_name"] +" "+ hex(db["from"]))
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1

        elif text == "Strings":
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText((base64.b64decode(db["string"])).decode())
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1

        elif text == "All":
            projInfo = projectDb["functions"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText(db["signature"])
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
            projInfo = projectDb["string"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText((base64.b64decode(db["string"])).decode())
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
            projInfo = projectDb["structures"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText("recv "+db["fcn_name"] +" "+ hex(db["from"]))
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1
            projInfo = projectDb["imports"]
            cursor = projInfo.find()
            for db in cursor:
                checkBoxRecv = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
                checkBoxRecv.setText(db["name"]+" "+db["type"])
                self.gridLayout_4.addWidget(checkBoxRecv, i, 0, 1, 1)
                i += 1