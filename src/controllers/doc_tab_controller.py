from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os, sys, re

"""
TODO:  
Add more documentation sections
Add a way to get it from a folder instead of hard coded. [probably not]
name_like_this -> Name Like This.
Make the "prettyfier" for the view portion of the code.
"""


# doc_list
# doc_search_bar
# detailed_view

class doc_tab_controller:

    def __init__(self, docTab):
        self.docs = {
            'demo': {'name': 'Demo',
                     'path': 'demo.html'},
            'documentation': {'name': 'Documentation',
                              'path': 'documentation.html'},
            'plugin': {'name': 'Plugin',
                       'path': 'plugin.html'},
            'analysis': {'name': 'Analysis',
                         'path': 'analysis.html'},
            'poi': {'name': 'Poi',
                    'path': 'poi.html'},
            'project': {'name': 'Project',
                        'path': 'project.html'},
        }

        self.doc_tab = docTab
        self.load_document_List(self.docs)
        self.get_documents(self.docs)

    def establish_connections(self):
        self.doc_tab.doc_list.itemSelectionChanged.connect(lambda: self.display_doc())

    def establish_calls(self):
        pass

    def load_document_List(self, docs):
        for doc in docs.keys():
            self.doc_tab.doc_list.addItem(str(self.docs[doc]['name']))

    def get_documents(self, docs):
        root = os.getcwd()
        for doc in docs.keys():
            path = root + '/resources/docs/' + self.docs[doc]['path']
            file = open(path, 'r', encoding='utf8')
            content = file.read()
            self.docs[doc]['content'] = content
            file.close()
            # print(content)
            self.doc_tab.detailed_view.setHtml(self.docs['demo']['content'])
            self.doc_tab.doc_list.setCurrentRow(0)

    def display_doc(self):
        selected = self.doc_tab.doc_list.currentItem().text()
        print(selected)
        print('it changed')
        self.doc_tab.detailed_view.setHtml(self.docs[selected.lower()]['content'])
