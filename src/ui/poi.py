# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_POI_tab(QtWidgets.QWidget):
    def setupUi(self, POI_tab):
        POI_tab.setObjectName("POI_tab")
        POI_tab.resize(729, 515)
        self.horizontalLayout = QtWidgets.QHBoxLayout(POI_tab)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.POI_frame = QtWidgets.QVBoxLayout()
        self.POI_frame.setObjectName("POI_frame")

        self.POI_list_frame = QtWidgets.QLabel(POI_tab)
        self.POI_list_frame.setObjectName("POI_list_frame")
        self.POI_frame.addWidget(self.POI_list_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.button_POI_search = QtWidgets.QLineEdit(POI_tab)
        self.button_POI_search.setObjectName("button_POI_search")
        self.POI_frame.addWidget(self.button_POI_search, 0, QtCore.Qt.AlignHCenter)

        self.POI_list_view = QtWidgets.QFrame(POI_tab)
        self.POI_list_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.POI_list_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.POI_list_view.setObjectName("POI_list_view")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.POI_list_view)
        self.verticalLayout.setObjectName("verticalLayout")

        self.POI = QtWidgets.QPushButton(self.POI_list_view)
        self.POI.setFlat(True)
        self.POI.setObjectName("POI")
        self.verticalLayout.addWidget(self.POI)

        self.POI_2 = QtWidgets.QPushButton(self.POI_list_view)
        self.POI_2.setFlat(True)
        self.POI_2.setObjectName("POI_2")
        self.verticalLayout.addWidget(self.POI_2)

        self.POI_3 = QtWidgets.QPushButton(self.POI_list_view)
        self.POI_3.setFlat(True)
        self.POI_3.setObjectName("POI_3")
        self.verticalLayout.addWidget(self.POI_3)
        self.POI_frame.addWidget(self.POI_list_view)

        self.POI_4 = QtWidgets.QPushButton(self.POI_list_view)
        self.POI_4.setFlat(True)
        self.POI_4.setObjectName("POI_4")
        self.verticalLayout.addWidget(self.POI_4)

        self.POI_5 = QtWidgets.QPushButton(self.POI_list_view)
        self.POI_5.setFlat(True)
        self.POI_5.setObjectName("POI_5")
        self.verticalLayout.addWidget(self.POI_5)


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.POI_frame.addItem(spacerItem)

        self.button_POI_new = QtWidgets.QPushButton(POI_tab)
        self.button_POI_new.setObjectName("button_POI_new")
        self.POI_frame.addWidget(self.button_POI_new, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.POI_frame)

        self.POI_detailed_frame = QtWidgets.QVBoxLayout()
        self.POI_detailed_frame.setObjectName("POI_detailed_frame")

        self.POI_deailed_label = QtWidgets.QLabel(POI_tab)
        self.POI_deailed_label.setObjectName("POI_deailed_label")
        self.POI_detailed_frame.addWidget(self.POI_deailed_label, 0, QtCore.Qt.AlignHCenter)

        self.POI_filter_frame = QtWidgets.QFrame(POI_tab)
        self.POI_filter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.POI_filter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.POI_filter_frame.setObjectName("POI_filter_frame")

        self.formLayout = QtWidgets.QFormLayout(self.POI_filter_frame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")

        self.comboBox_plugin = QtWidgets.QComboBox(self.POI_filter_frame)
        self.comboBox_plugin.setObjectName("comboBox_plugin")
        self.comboBox_plugin.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_plugin)

        self.POI_type_label = QtWidgets.QLabel(self.POI_filter_frame)
        self.POI_type_label.setObjectName("POI_type_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.POI_type_label)

        self.comboBox_POI_type = QtWidgets.QComboBox(self.POI_filter_frame)
        self.comboBox_POI_type.setObjectName("comboBox_POI_type")
        self.comboBox_POI_type.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_POI_type)

        self.plugin_label = QtWidgets.QLabel(self.POI_filter_frame)
        self.plugin_label.setObjectName("plugin_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.plugin_label)
        self.POI_detailed_frame.addWidget(self.POI_filter_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.POI_content_area = QtWidgets.QTextEdit(POI_tab)
        self.POI_content_area.setObjectName("POI_content_area")
        self.POI_detailed_frame.addWidget(self.POI_content_area)

        self.POI_creation_frame = QtWidgets.QHBoxLayout()
        self.POI_creation_frame.setObjectName("POI_creation_frame")

        self.button_save_POI = QtWidgets.QPushButton(POI_tab)
        self.button_save_POI.setObjectName("button_save_POI")
        self.POI_creation_frame.addWidget(self.button_save_POI)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.POI_creation_frame.addItem(spacerItem1)
        self.button_delete_POI = QtWidgets.QPushButton(POI_tab)

        self.button_delete_POI.setObjectName("button_delete_POI")
        self.POI_creation_frame.addWidget(self.button_delete_POI)
        self.POI_detailed_frame.addLayout(self.POI_creation_frame)
        self.horizontalLayout.addLayout(self.POI_detailed_frame)

        self.retranslateUi(POI_tab)
        QtCore.QMetaObject.connectSlotsByName(POI_tab)

    def retranslateUi(self, POI_tab):
        _translate = QtCore.QCoreApplication.translate
        POI_tab.setWindowTitle(_translate("POI_tab", "Frame"))
        self.POI_list_frame.setText(_translate("POI_tab", "Point Of Interest View"))
        self.button_POI_search.setText(_translate("POI_tab", "search POI"))
        self.POI.setText(_translate("POI_tab", "Point of Interest A"))
        self.POI_2.setText(_translate("POI_tab", "Point of Interest B"))
        self.POI_3.setText(_translate("POI_tab", "Point of Interest C"))
        self.POI_4.setText(_translate("POI_tab", "Point Of Interest D"))
        self.POI_5.setText(_translate("POI_tab", "Point of Interest E"))
        self.button_POI_new.setText(_translate("POI_tab", "New"))
        self.POI_deailed_label.setText(_translate("POI_tab", "Detailed Point Of Interest View "))
        self.comboBox_plugin.setItemText(0, _translate("POI_tab", "Existing Plugin"))
        self.POI_type_label.setText(_translate("POI_tab", "Point Of Interest View"))
        self.comboBox_POI_type.setItemText(0, _translate("POI_tab", "Type of Point Of Interest"))
        self.plugin_label.setText(_translate("POI_tab", "Plugin"))
        self.button_save_POI.setText(_translate("POI_tab", "Delete"))
        self.button_delete_POI.setText(_translate("POI_tab", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    POI_tab = QtWidgets.QFrame()
    ui = Ui_POI_tab()
    ui.setupUi(POI_tab)
    POI_tab.show()
    sys.exit(app.exec_())
