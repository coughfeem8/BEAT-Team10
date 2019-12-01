from PyQt5 import QtCore, QtGui, QtWidgets


class Tab5(QtWidgets.QWidget):
    def __init__(self, parent, main):
        QtWidgets.QWidget.__init__(self, parent)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setObjectName("Frame")
        self.frame.resize(770, 586)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.doc_label = QtWidgets.QLabel(self.frame)
        self.doc_label.setObjectName("doc_label")
        self.verticalLayout.addWidget(self.doc_label, 0, QtCore.Qt.AlignHCenter)

        self.doc_search_bar = QtWidgets.QLineEdit(self.frame)
        self.doc_search_bar.setObjectName("doc_search_bar")
        self.doc_search_bar.addAction(QtGui.QIcon("resources/search.png"), QtWidgets.QLineEdit.LeadingPosition)
        self.verticalLayout.addWidget(self.doc_search_bar, 0, QtCore.Qt.AlignHCenter)

        self.doc_list = QtWidgets.QListWidget(self.frame)
        self.doc_list.setObjectName("doc_list")
        self.verticalLayout.addWidget(self.doc_list)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.detailed_view = QtWidgets.QTextBrowser(self.frame)
        self.detailed_view.setObjectName("detailed_view")
        self.horizontalLayout.addWidget(self.detailed_view)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        QtCore.QMetaObject.connectSlotsByName(self.frame)

        _translate = QtCore.QCoreApplication.translate
        self.frame.setWindowTitle(_translate("Frame", "Frame"))
        self.doc_label.setText(_translate("Frame", "Documentation"))
