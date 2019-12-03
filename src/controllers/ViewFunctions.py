from PyQt5 import QtCore, QtWidgets


class ViewFunctions(QtCore.QObject):

    def create_operations(self, signal, buttons_to_disable, buttons_to_enable, list_to_disable):
        """
        This function enables and disables the buttons depending on the operation that can be preform at the
        moment.
        :param signal:
        :param buttons_to_disable:
        :param buttons_to_enable:
        :param list_to_disable:
        :return:
        """
        signal.emit()
        for button in buttons_to_disable:
            button.setEnabled(False)
        for button in buttons_to_enable:
            button.setEnabled(True)
        for item_index in range(list_to_disable.count()):
            item = list_to_disable.item(item_index)
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable)

    def delete_save_operations(self, signal, buttons_to_enable, buttons_to_disable, list_to_enable):
        """
        This function enables and disables the buttons depending on the operation that can be preform at the
        moment
        :param signal:
        :param buttons_to_enable:
        :param buttons_to_disable:
        :param list_to_enable:
        :return:
        """
        signal.emit()
        for button in buttons_to_enable:
            button.setEnabled(True)
        for button in buttons_to_disable:
            button.setEnabled(False)
        for item_index in range(list_to_enable.count()):
            item = list_to_enable.item(item_index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsSelectable)

    def search_list(self, listWidget, text):
        """
        This function accepts input form the user to search a point of interest from a typed word in the search
        bar.
        :param listWidget:
        :param text:
        :return:
        """
        if len(text) is not 0:
            search_result = listWidget.findItems(text, QtCore.Qt.MatchContains)
            for item_index in range(listWidget.count()):
                listWidget.item(item_index).setHidden(True)
            for item_index in search_result:
                item_index.setHidden(False)
        else:
            for item_index in range(listWidget.count()):
                listWidget.item(item_index).setHidden(False)
