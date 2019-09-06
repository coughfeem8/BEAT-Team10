from PyQt5 import QtCore, QtGui, QtWidgets

def fillTab5():


    documentationTab = QtWidgets.QWidget()
    documentationTab.setObjectName("documentationTab")
    frame_4 = QtWidgets.QFrame(documentationTab)
    frame_4.setGeometry(QtCore.QRect(20, 10, 161, 550))
    frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_4.setObjectName("frame_4")
    label_14 = QtWidgets.QLabel(frame_4)
    label_14.setGeometry(QtCore.QRect(10, 10, 131, 21))
    label_14.setAlignment(QtCore.Qt.AlignCenter)
    label_14.setObjectName("label_14")
    textEdit_3 = QtWidgets.QTextEdit(frame_4)
    textEdit_3.setGeometry(QtCore.QRect(10, 40, 141, 31))
    textEdit_3.setObjectName("textEdit_3")
    label_15 = QtWidgets.QLabel(frame_4)
    label_15.setGeometry(QtCore.QRect(10, 90, 146, 16))
    label_15.setObjectName("label_15")
    label_16 = QtWidgets.QLabel(frame_4)
    label_16.setGeometry(QtCore.QRect(10, 110, 141, 17))
    label_16.setAlignment(QtCore.Qt.AlignCenter)
    label_16.setObjectName("label_16")
    frame_5 = QtWidgets.QFrame(documentationTab)
    frame_5.setGeometry(QtCore.QRect(199, 9, 581, 550))
    frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_5.setObjectName("frame_5")
    frame_6 = QtWidgets.QFrame(frame_5)
    frame_6.setGeometry(QtCore.QRect(19, 49, 541, 461))
    frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_6.setObjectName("frame_6")
    label_17 = QtWidgets.QLabel(frame_6)
    label_17.setGeometry(QtCore.QRect(180, 170, 171, 17))
    label_17.setObjectName("label_17")
    label_18 = QtWidgets.QLabel(frame_5)
    label_18.setGeometry(QtCore.QRect(200, 10, 171, 17))
    label_18.setObjectName("label_18")

    _translate = QtCore.QCoreApplication.translate

    label_14.setText(_translate("MainWindow", "Document View"))
    label_15.setText(_translate("MainWindow", "BEAT Documentation"))
    label_16.setText(_translate("MainWindow", "Plug In Structure"))
    label_17.setText(_translate("MainWindow", "Document Content Area"))
    label_18.setText(_translate("MainWindow", "Detailed Document View"))

    return documentationTab