from PyQt5 import QtWidgets


class ErrorDialog(QtWidgets.QMessageBox):
    def __init__(self, parent, text, title):
        QtWidgets.QMessageBox.__init__(self, parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def exec_(self):
        super(ErrorDialog, self).exec_()
        return
