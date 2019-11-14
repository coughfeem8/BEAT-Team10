# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'documentation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(770, 586)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.doc_label = QtWidgets.QLabel(Frame)
        self.doc_label.setObjectName("doc_label")
        self.verticalLayout.addWidget(self.doc_label, 0, QtCore.Qt.AlignHCenter)
        self.doc_search_bar = QtWidgets.QLineEdit(Frame)
        self.doc_search_bar.setObjectName("doc_search_bar")
        self.verticalLayout.addWidget(self.doc_search_bar, 0, QtCore.Qt.AlignHCenter)
        self.doc_list = QtWidgets.QListWidget(Frame)
        self.doc_list.setObjectName("doc_list")
        self.verticalLayout.addWidget(self.doc_list)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.detailed_view = QtWidgets.QTextBrowser(Frame)
        self.detailed_view.setObjectName("detailed_view")
        self.horizontalLayout.addWidget(self.detailed_view)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.doc_label.setText(_translate("Frame", "Documentation"))

