from PyQt5 import QtWidgets


class PopUpDialog(QtWidgets.QDialog):
    def exec_(self):
        super(PopUpDialog, self).exec_()
        return self.returnVal

    def save_text(self):
        self.returnVal = self.textEdit.toPlainText()
        self.accept()

    def clear_text(self):
        self.returnVal = ""
        self.accept()
