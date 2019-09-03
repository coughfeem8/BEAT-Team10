from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def fillTab1(widget, parent):
    widget.layout = QHBoxLayout()

    frameProj = QFrame()
    frameProj.setFrameShape(QFrame.StyledPanel)
    frameProj.setLineWidth(0.6)
    frameProj.setMaximumWidth(parent.width / 5)
    frameDet = QFrame()
    frameDet.setFrameShape(QFrame.StyledPanel)
    frameDet.setLineWidth(0.6)

    titleFont = QFont("Times", 15, QFont.Bold)

    #Project View
    lblProjView = QLabel("Project View", frameProj)
    lblProjView.move((frameProj.width()-lblProjView.width())/3, 5)
    lblProjView.setFont(titleFont)
    txtSearch = QLineEdit(frameProj)
    txtSearch.setClearButtonEnabled(True)
    txtSearch.addAction(QIcon("resources/search.png"), QLineEdit.LeadingPosition)
    txtSearch.setPlaceholderText("Search...")
    txtSearch.move(15, lblProjView.height()+10)
    listProject = QListWidget(frameProj)
    listProject.move(5, lblProjView.height()+50)
    listProject.setMaximumWidth(frameProj.width()-10)
    listProject.setMinimumHeight(frameProj.height()+150)
    listProject.insertItem(0, "Project A")
    listProject.insertItem(1, "Project B")
    listProject.insertItem(2, "Project C")
    listProject.insertItem(3, "Project D")
    listProject.setStyleSheet('''QWidget {border:none;}''')
    btnNewProj = QPushButton("New", frameProj)
    btnNewProj.move(70, frameProj.height()+220)

    #Project Detailed View
    lblProjDet = QLabel("Detailed Project View", frameDet)
    lblProjDet.move((frameDet.width()-lblProjDet.width())/3, 5)
    lblProjDet.setFont(titleFont)


    widget.layout.addWidget(frameProj)
    widget.layout.addWidget(frameDet)
    return widget.layout
