from PyQt5 import QtCore, QtGui, QtWidgets
import pop
import r2pipe
import base64
from singleton import Singleton
import pymongo


class Tab2(QtWidgets.QWidget):
    def __init__(self, parent, main):
        QtWidgets.QWidget.__init__(self, parent)
        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setObjectName("gridLayout")
        plugin_label = QtWidgets.QLabel(self)
        plugin_label.setAlignment(QtCore.Qt.AlignCenter)
        plugin_label.setObjectName("plugin_label")
        gridLayout.addWidget(plugin_label, 0, 0, 1, 1)
        plugin_comboBox = QtWidgets.QComboBox(self)
        plugin_comboBox.setMaxVisibleItems(10)
        plugin_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        plugin_comboBox.setObjectName("plugin_comboBox")
        plugin_comboBox.addItem("")
        plugin_comboBox.addItem("")
        plugin_comboBox.addItem("")
        gridLayout.addWidget(plugin_comboBox, 0, 1, 1, 1)
        static_anal_label = QtWidgets.QLabel(self)
        static_anal_label.setAlignment(QtCore.Qt.AlignCenter)
        static_anal_label.setObjectName("static_anal_label")
        gridLayout.addWidget(static_anal_label, 1, 0, 1, 1)
        static_run_button = QtWidgets.QPushButton(self)
        static_run_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        static_run_button.setObjectName("static_run_button")
        static_run_button.clicked.connect(self.staticAna)
        gridLayout.addWidget(static_run_button, 1, 1, 1, 1)
        dynamic_anal_label = QtWidgets.QLabel(self)
        dynamic_anal_label.setAlignment(QtCore.Qt.AlignCenter)
        dynamic_anal_label.setObjectName("dynamic_anal_label")
        gridLayout.addWidget(dynamic_anal_label, 1, 2, 1, 1)
        dynamic_run_button = QtWidgets.QPushButton(self)
        dynamic_run_button.setObjectName("dynamic_run_button")
        #dynamic_run_button.clicked.connect(self.runDynamicAnalysis)
        gridLayout.addWidget(dynamic_run_button, 1, 3, 1, 1)
        dynamic_stop_button = QtWidgets.QPushButton(self)
        dynamic_stop_button.setObjectName("dynamic_stop_button")
        gridLayout.addWidget(dynamic_stop_button, 1, 4, 1, 2)
        poi_label = QtWidgets.QLabel(self)
        poi_label.setAlignment(QtCore.Qt.AlignCenter)
        poi_label.setObjectName("poi_label")
        gridLayout.addWidget(poi_label, 2, 0, 1, 1)
        self.poi_comboBox = QtWidgets.QComboBox(self)
        self.poi_comboBox.setObjectName("poi_comboBox")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")
        self.poi_comboBox.addItem("")

        gridLayout.addWidget(self.poi_comboBox, 2, 1, 1, 1)
        gridLayout_6 = QtWidgets.QGridLayout()
        gridLayout_6.setObjectName("gridLayout_6")
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        search_bar_lineEdit = QtWidgets.QLineEdit(self)
        search_bar_lineEdit.setFrame(True)
        search_bar_lineEdit.setObjectName("search_bar_lineEdit")
        search_bar_lineEdit.addAction(QtGui.QIcon("resources/search.png"), QtWidgets.QLineEdit.LeadingPosition)
        horizontalLayout.addWidget(search_bar_lineEdit)
        gridLayout_6.addLayout(horizontalLayout, 1, 1, 1, 1)
        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 243, 222))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        gridLayout_6.addWidget(scrollArea, 2, 1, 1, 1)
        poi_title_label = QtWidgets.QLabel(self)
        poi_title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        poi_title_label.setAutoFillBackground(False)
        poi_title_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(0, 170, 255);")
        poi_title_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        poi_title_label.setObjectName("poi_title_label")
        gridLayout_6.addWidget(poi_title_label, 0, 1, 1, 1)
        gridLayout.addLayout(gridLayout_6, 3, 0, 2, 2)
        a_pushButton = QtWidgets.QPushButton(self)
        a_pushButton.setMaximumSize(QtCore.QSize(16, 20))
        a_pushButton.clicked.connect(self.openAnalysis)
        a_pushButton.setObjectName("a_pushButton")
        gridLayout.addWidget(a_pushButton, 3, 5, 1, 1)
        scrollArea_2 = QtWidgets.QScrollArea(self)
        scrollArea_2.setWidgetResizable(True)
        scrollArea_2.setObjectName("scrollArea_2")
        scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 373, 253))
        scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        gridLayout_2 = QtWidgets.QGridLayout(scrollAreaWidgetContents_3)
        gridLayout_2.setObjectName("gridLayout_2")
        self.poi_content_area_textEdit = QtWidgets.QTextEdit(scrollAreaWidgetContents_3)
        self.poi_content_area_textEdit.setObjectName("poi_content_area_textEdit")
        gridLayout_2.addWidget(self.poi_content_area_textEdit, 0, 0, 1, 1)
        c_pushButton = QtWidgets.QPushButton(scrollAreaWidgetContents_3)
        c_pushButton.setMaximumSize(QtCore.QSize(16, 20))
        c_pushButton.clicked.connect(self.openComment)
        c_pushButton.setObjectName("c_pushButton")
        gridLayout_2.addWidget(c_pushButton, 0, 1, 1, 1)
        terminal_window_lineEdit = QtWidgets.QLineEdit(scrollAreaWidgetContents_3)
        terminal_window_lineEdit.setObjectName("terminal_window_lineEdit")
        gridLayout_2.addWidget(terminal_window_lineEdit, 1, 0, 1, 1)
        scrollArea_2.setWidget(scrollAreaWidgetContents_3)
        gridLayout.addWidget(scrollArea_2, 4, 2, 1, 3)
        o_pushButton = QtWidgets.QPushButton(self)
        o_pushButton.setMaximumSize(QtCore.QSize(16, 20))
        o_pushButton.clicked.connect(self.openOutput)
        o_pushButton.setObjectName("o_pushButton")
        gridLayout.addWidget(o_pushButton, 4, 5, 1, 1)
        detailed_poi_view_label = QtWidgets.QLabel(self)
        detailed_poi_view_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                                   "background-color: rgb(0, 170, 255);")
        detailed_poi_view_label.setAlignment(QtCore.Qt.AlignCenter)
        detailed_poi_view_label.setObjectName("detailed_poi_view_label")
        gridLayout.addWidget(detailed_poi_view_label, 3, 2, 1, 3)

        self.poi_comboBox.currentIndexChanged.connect(lambda x: self.poiComBxChng(text = self.poi_comboBox.currentText()))

        _translate = QtCore.QCoreApplication.translate

        plugin_label.setText(_translate("MainWindow", "Plugin"))
        plugin_comboBox.setItemText(0, _translate("MainWindow", "Plugin A"))
        plugin_comboBox.setItemText(1, _translate("MainWindow", "Plugin B"))
        plugin_comboBox.setItemText(2, _translate("MainWindow", "Plugin C"))
        static_anal_label.setText(_translate("MainWindow", "Static Analysis"))
        static_run_button.setText(_translate("MainWindow", "Run"))
        dynamic_anal_label.setText(_translate("MainWindow", "Dynamic Analysis"))
        dynamic_run_button.setText(_translate("MainWindow", "Run"))
        dynamic_stop_button.setText(_translate("MainWindow", "Stop"))
        poi_label.setText(_translate("MainWindow", "Point of Interest"))
        self.poi_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.poi_comboBox.setItemText(1, _translate("MainWindow", "Functions"))
        self.poi_comboBox.setItemText(2, _translate("MainWindow", "Structs"))
        self.poi_comboBox.setItemText(3, _translate("MainWindow", "Strings"))
        self.poi_comboBox.setItemText(4, _translate("MainWindow", "DLL"))
        poi_title_label.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-weight:600;\">Point of Interest View</span></p></body></html>"))
        a_pushButton.setText(_translate("MainWindow", "A"))
        c_pushButton.setText(_translate("MainWindow", "C"))
        o_pushButton.setText(_translate("MainWindow", "O"))
        detailed_poi_view_label.setText(_translate("MainWindow",
                                                    "<html><head/><body><p><span style=\" font-weight:600;\">Detailed Point of Interst View</span></p></body></html>"))


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