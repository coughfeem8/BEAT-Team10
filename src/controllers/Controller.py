from PyQt5 import QtCore, QtWidgets


class Controller(QtCore.QObject):
    def create_operations(self, signal, buttons_to_disable, buttons_to_enable, list_to_disable):
        signal.emit()
        for button in buttons_to_disable:
            button.setEnabled(False)
        for button in buttons_to_enable:
            button.setEnabled(True)
        for item_index in range(list_to_disable.count()):
            item = list_to_disable.item(item_index)
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable)

    def delete_save_operations(self, signal, buttons_to_enable, buttons_to_disable, list_to_enable):
        signal.emit()
        for button in buttons_to_enable:
            button.setEnabled(True)
        for button in buttons_to_disable:
            button.setEnabled(False)
        for item_index in range(list_to_enable.count()):
            item = list_to_enable.item(item_index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsSelectable)

    def search_list(self, listWidget, text):
        if len(text) is not 0:
            search_result = listWidget.findItems(text, QtCore.Qt.MatchContains)
            for item_index in range(listWidget.count()):
                listWidget.item(item_index).setHidden(True)
            for item_index in search_result:
                item_index.setHidden(False)
        else:
            for item_index in range(listWidget.count()):
                listWidget.item(item_index).setHidden(False)
