import os
from view.ui_implementation.ViewFunctions import ViewFunctions

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


class DocumentationTabImplementation(ViewFunctions):

    def __init__(self, documentation_tab):
        super().__init__()
        self.docs = {
            'beat': {'name': 'Beat',
                     'path': 'beat.html'},
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

        self.documentation_tab = documentation_tab
        self.load_document_list(self.docs)
        self.get_documents(self.docs)

    def establish_connections(self):
        self.documentation_tab.doc_list.itemSelectionChanged.connect(lambda: self.display_doc())
        self.documentation_tab.doc_search_bar.textChanged.connect(
            lambda: self.search_list(self.documentation_tab.doc_list, self.documentation_tab.doc_search_bar.text()))

    def establish_calls(self):
        pass

    def load_document_list(self, docs):
        """
        This method loads all the documentation and displays it in the list holding all the available
        documentation.
        :param docs: all installed documents
        :return: none
        """
        for doc in docs.keys():
            self.documentation_tab.doc_list.addItem(str(self.docs[doc]['name']))

    def get_documents(self, docs):
        """
        This method get the documentation from the resources folder and add them into the doc list.
        :param docs: installed documents
        :return: none
        """
        root = os.getcwd()
        for doc in docs.keys():
            path = root + '/resources/docs/' + self.docs[doc]['path']
            file = open(path, 'r', encoding='utf8')
            content = file.read()
            self.docs[doc]['content'] = content
            file.close()
            self.documentation_tab.detailed_view.setHtml(self.docs['beat']['content'])
            self.documentation_tab.doc_list.setCurrentRow(0)

    def display_doc(self):
        """
        This method depending on the selected document displays it into the documentation view
        :return: none
        """
        selected = self.documentation_tab.doc_list.currentItem().text()
        self.documentation_tab.detailed_view.setHtml(self.docs[selected.lower()]['content'])
